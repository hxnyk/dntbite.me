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
    account_sid = os.environ.get("TWILIO_SID")
    auth_token = os.environ.get("TWILIO_AUTH")
    client = TwilioRestClient(account_sid, auth_token)
    message = client.messages.create(body=message,
        to=number,
        from_="2262402483")
    print message.sid


port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)