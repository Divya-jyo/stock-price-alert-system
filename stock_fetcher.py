import requests
import time
from database import save_price

API_KEY = "OQLKSHKTVUG57BGA"


def get_stock_price(symbol):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if "Global Quote" in data and data["Global Quote"]:
        price = float(data["Global Quote"]["05. price"])
        change = data["Global Quote"]["10. change percent"]
        print(f"Stock: {symbol} | Price: ${price} | Change: {change}")

        # Save to database
        save_price(symbol, price, change)
        return price
    else:
        print(f"Error fetching {symbol}")
        return None


# Fetch and save prices
symbols = ["AAPL", "GOOGL", "TSLA"]

for symbol in symbols:
    get_stock_price(symbol)
    print("Waiting 15 seconds...")
    time.sleep(15)