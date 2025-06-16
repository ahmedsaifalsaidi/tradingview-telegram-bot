from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=payload)

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    print(f"Received: {data}")
    if data.get("signal") == "buy":
        send_telegram_message("📈 إشـارة شـراء من TradingView!")
    elif data.get("signal") == "sell":
        send_telegram_message("📉 إشـارة بيـع من TradingView!")
    return "OK", 200
