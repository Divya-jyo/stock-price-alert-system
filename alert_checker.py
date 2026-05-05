import boto3
import os
from stock_fetcher import get_stock_price
from database import get_active_alerts, disable_alert

# AWS SNS connection
sns = boto3.client("sns", region_name="us-east-2")
SNS_TOPIC_ARN = "arn:aws:sns:us-east-2:424999960716:StockAlerts"

def check_and_alert():
    print("🔍 Checking all active alerts...")

    alerts = get_active_alerts()

    if not alerts:
        print("No active alerts found.")
        return

    for alert in alerts:
        print(f"Checking {alert.stock_symbol}...")

        # Get current price from Alpha Vantage
        current_price = get_stock_price(alert.stock_symbol)

        if current_price is None:
            print(f"❌ Could not fetch price for {alert.stock_symbol}")
            continue

        print(f"Current Price: ${current_price} | Your threshold: {alert.condition} ${alert.threshold_price}")

        # Check if price crossed threshold
        triggered = False

        if alert.condition == "above" and current_price > alert.threshold_price:
            triggered = True
        elif alert.condition == "below" and current_price < alert.threshold_price:
            triggered = True

        if triggered:
            print(f"🚨 Alert triggered for {alert.stock_symbol}!")
            send_email(alert, current_price)
            disable_alert(alert.id)
        else:
            print(f"✅ No alert needed for {alert.stock_symbol} yet.")

def send_email(alert, current_price):
    message = (
        f"🚨 Stock Alert Triggered!\n\n"
        f"Stock: {alert.stock_symbol}\n"
        f"Current Price: ${current_price:.2f}\n"
        f"Your condition: price goes {alert.condition} ${alert.threshold_price}\n\n"
        f"This alert has been deactivated automatically."
    )

    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=message,
        Subject=f"🚨 Stock Alert: {alert.stock_symbol}"
    )
    print(f"✅ Email alert sent!")

# Run it
if __name__ == "__main__":
    check_and_alert()