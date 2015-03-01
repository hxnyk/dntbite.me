# Main web server
from flask import Flask, request, send_from_directory, redirect
from twilio.rest import TwilioRestClient
import os

app = Flask(__name__)
app.config['DEBUG'] = True

def send_message_to(number, message):
    account_sid = os.environ.get("TWILIO_SID")
    auth_token = os.environ.get("TWILIO_AUTH")
    client = TwilioRestClient(account_sid, auth_token)
    message = client.messages.create(body=message,
        to=number,
        from_="2262402483")

@app.route("/")
def home():
    return send_from_directory(os.getcwd(), "static/index.html")

@app.route("/signup", methods=['POST'])
def new_user():
    name = request.form["newname"]
    password = request.form["newpassword"]
    email  = request.form["newemail"]
    phone_no = request.form["newnumber"]

@app.route("/bite", methods=['POST'])
def bite():
    #send_message_to("4407592260", "Stop biting your nails!!!")
    return "Bite"

@app.route("/<file_name>.<ext>")
def send_file(file_name, ext):
    return redirect('/static/' + file_name + '.' + ext)

port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)