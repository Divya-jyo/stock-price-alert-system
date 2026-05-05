from flask import Flask, request, jsonify
from database import save_alert, get_active_alerts, Session, Alert

app = Flask(__name__)

# ✅ Home - just to check app is running
@app.route("/")
def home():
    return jsonify({"message": "Stock Alert System is Running! ✅"})

# ✅ Create a new alert
@app.route("/alert", methods=["POST"])
def create_alert():
    data = request.get_json()

    save_alert(
        email=data["email"],
        symbol=data["symbol"].upper(),
        threshold_price=data["threshold_price"],
        condition=data["condition"]   # "above" or "below"
    )

    return jsonify({"message": f"Alert created for {data['symbol']}!"}), 201

# ✅ View all active alerts
@app.route("/alerts", methods=["GET"])
def view_alerts():
    alerts = get_active_alerts()
    result = [
        {
            "id": a.id,
            "email": a.user_email,
            "symbol": a.stock_symbol,
            "threshold": a.threshold_price,
            "condition": a.condition
        }
        for a in alerts
    ]
    return jsonify(result), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)