"""
AWS Lambda Handler — Real-Time Stock Price Alert System
Divya Jyothi Karri | 2026

Triggered every 5 minutes via AWS EventBridge.
Fetches stock prices → stores in PostgreSQL (RDS) → sends SNS alerts on threshold breach.
"""

import json
import os
import logging
import boto3
import pg8000
import requests
from datetime import datetime

# ── Logging ───────────────────────────────────────────────────────────────────
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# ── Environment Variables (set in Lambda console) ─────────────────────────────
DB_HOST               = os.environ.get("DB_HOST")
DB_PORT               = os.environ.get("DB_PORT", "5432")
DB_NAME               = os.environ.get("DB_NAME")
DB_USER               = os.environ.get("DB_USER")
DB_PASSWORD           = os.environ.get("DB_PASSWORD")
ALPHA_VANTAGE_API_KEY = os.environ.get("ALPHA_VANTAGE_API_KEY")
SNS_TOPIC_ARN         = os.environ.get("SNS_TOPIC_ARN", "arn:aws:sns:us-east-2:424999960716:StockAlerts")
AWS_REGION            = os.environ.get("AWS_REGION", "us-east-2")

ALPHA_VANTAGE_URL = "https://www.alphavantage.co/query"
sns_client = boto3.client("sns", region_name=AWS_REGION)


# ── Database Helpers ──────────────────────────────────────────────────────────

def get_db_connection():
    return pg8000.connect(
        host=DB_HOST,
        port=int(DB_PORT),
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

def get_alert_rules(conn):
    """
    Fetch all active alert rules from the database.
    Returns list of dicts: {id, symbol, threshold_price, direction}
    direction = 'above' or 'below'
    """
    with conn.cursor() as cur:
        cur.execute("""
            SELECT id, symbol, threshold_price, direction
            FROM alert_rules
            WHERE is_active = TRUE
        """)
        rows = cur.fetchall()
    return [
        {
            "id":               row[0],
            "symbol":           row[1],
            "threshold_price":  float(row[2]),
            "direction":        row[3],
        }
        for row in rows
    ]


def store_price(conn, symbol: str, price: float):
    """Insert a fetched price into the stock_prices table."""
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO stock_prices (symbol, price, fetched_at)
            VALUES (%s, %s, %s)
        """, (symbol, price, datetime.utcnow()))
    conn.commit()
    logger.info(f"Stored price: {symbol} = ${price:.2f}")


# ── Alpha Vantage Helper ──────────────────────────────────────────────────────

def fetch_stock_price(symbol: str):
    """
    Fetch the latest stock price from Alpha Vantage.
    Returns float price or None on error.
    """
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol":   symbol,
        "apikey":   ALPHA_VANTAGE_API_KEY,
    }
    try:
        response = requests.get(ALPHA_VANTAGE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        quote     = data.get("Global Quote", {})
        price_str = quote.get("05. price")

        if not price_str:
            logger.warning(f"No price returned for {symbol}: {data}")
            return None

        return float(price_str)

    except requests.RequestException as exc:
        logger.error(f"HTTP error fetching {symbol}: {exc}")
        return None
    except (ValueError, KeyError) as exc:
        logger.error(f"Parse error for {symbol}: {exc}")
        return None


# ── SNS Alert Helper ──────────────────────────────────────────────────────────

def send_alert(symbol: str, price: float, threshold: float, direction: str):
    """Publish an SNS notification when a threshold is crossed."""
    subject = f"Stock Alert: {symbol} price {direction} threshold"
    message = (
        f"Stock Alert Triggered!\n\n"
        f"  Symbol    : {symbol}\n"
        f"  Current   : ${price:.2f}\n"
        f"  Threshold : ${threshold:.2f}\n"
        f"  Condition : Price is {direction} threshold\n"
        f"  Time      : {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC\n\n"
        f"Login to your dashboard to review this alert."
    )
    try:
        response = sns_client.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject=subject,
            Message=message,
        )
        logger.info(f"SNS alert sent for {symbol}. MessageId: {response['MessageId']}")
    except Exception as exc:
        logger.error(f"Failed to send SNS alert for {symbol}: {exc}")


# ── Alert Checker ─────────────────────────────────────────────────────────────

def check_and_alert(rule: dict, price: float):
    """Check if price crosses threshold and send alert if needed."""
    symbol    = rule["symbol"]
    threshold = rule["threshold_price"]
    direction = rule["direction"]

    triggered = (
        (direction == "above" and price >= threshold) or
        (direction == "below" and price <= threshold)
    )

    if triggered:
        logger.info(f"ALERT triggered: {symbol} ${price:.2f} is {direction} ${threshold:.2f}")
        send_alert(symbol, price, threshold, direction)
    else:
        logger.info(f"No alert: {symbol} ${price:.2f} not {direction} ${threshold:.2f}")


# ── Main Lambda Handler ───────────────────────────────────────────────────────

def lambda_handler(event, context):
    """
    Main entry point for AWS Lambda.
    Called every 5 minutes by EventBridge.
    """
    logger.info("Lambda triggered — starting stock price check.")

    results = {"checked": [], "alerted": [], "errors": [], "skipped": []}
    conn = None

    try:
        conn = get_db_connection()
        logger.info("Database connection established.")

        rules = get_alert_rules(conn)
        if not rules:
            logger.info("No active alert rules found. Exiting.")
            return {"statusCode": 200, "body": json.dumps({"message": "No active rules"})}

        logger.info(f"Found {len(rules)} active alert rule(s).")

        # Fetch prices for unique symbols only (avoid duplicate API calls)
        symbols = list(set(rule["symbol"] for rule in rules))
        prices  = {}

        for symbol in symbols:
            price = fetch_stock_price(symbol)
            if price is not None:
                prices[symbol] = price
                store_price(conn, symbol, price)
                results["checked"].append({"symbol": symbol, "price": price})
            else:
                logger.warning(f"Could not fetch price for {symbol}. Skipping.")
                results["skipped"].append(symbol)

        # Check each rule
        for rule in rules:
            symbol = rule["symbol"]
            if symbol in prices:
                check_and_alert(rule, prices[symbol])


    except Exception as db_err:
        logger.error(f"Database error: {db_err}")
        return {"statusCode": 500, "body": json.dumps({"error": str(db_err)})}

    except Exception as exc:
        logger.error(f"Unexpected error: {exc}")
        return {"statusCode": 500, "body": json.dumps({"error": str(exc)})}

    finally:
        if conn:
            conn.close()
            logger.info("Database connection closed.")

    logger.info(f"Lambda complete. Results: {json.dumps(results)}")
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Stock check complete", "results": results})
    }