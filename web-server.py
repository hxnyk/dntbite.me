# Main web server
from flask import Flask, request
from twilio.rest import TwilioRestClient
import os

app = Flask(__name__)

def send_message_to(number, message):
    account_sid = os.environ.get("TWILIO_SID")
    auth_token = os.environ.get("TWILIO_AUTH")
    client = TwilioRestClient(account_sid, auth_token)
    message = client.messages.create(body=message,
        to=number,
        from_="2262402483")

@app.route("/")
def home():
    return "Hello"

@app.route("/bite", methods=['POST'])
def bite():
    send_message_to("4407592260", "Stop biting your nails!!!")
    return "Bite"

port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)