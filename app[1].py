from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    requests.post(url, data=payload)

@app.route("/alert", methods=["POST"])
def alert():
    data = request.json
    if data:
        message = f"🔔 <b>TradingView Alert</b> 🔔

{data.get('ticker', 'Unknown')} Alert:
{data.get('message', 'No details provided')}"
        send_telegram_message(message)
        return "Alert sent!", 200
    return "No data received", 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
