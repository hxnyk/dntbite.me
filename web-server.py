# Main web server
from flask import Flask
app = Flask(__name__)
from twilio.rest import TwilioRestClient

@app.route("/bite"i, methods=['POST'])
def bite():
    if (request.form["message"]):
        send_message_to("4407592260", "Stop biting your nails!!!")
        # add time to db for start
    else:
        pass
        # add time to db for end

def send_message_to(number, message):
    account_sid = ENV["TWILIO_SID"]
    auth_token = ENV["TWILIO_AUTH"]
    client = TwilioRestClient(account_sid, auth_token)
    message = client.messages.create(body=message,
        to=number, # Replace with your phone number
        from_="2262402483") # Replace with your Twilio number
    print message.sid
