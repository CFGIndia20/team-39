from twilio.rest import Client
import os

from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse

from twilio.base.exceptions import TwilioRestException

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')

client = Client(account_sid, auth_token)

# message = client.messages \
#                 .create(
#                      body="whatever the message we want that has been translated using google translate is to be put here",
#                      from_='+16262624030',
#                      to='+919893003147'
#                  )

# print(message.sid)


app = Flask(__name__)


@app.route("/answer", methods=['GET', 'POST'])
def answer():
    """Respond to incoming phone calls with a message."""
    # Start our TwiML response
    resp = VoiceResponse()

    caller = request.values.get('From')
    twilio_number = request.values.get('To')
    #send_sms(caller, twilio_number)

    # Read a message aloud to the caller
    resp.say("Thanks for calling! We just sent you a text with a clue.",
            voice='alice thanks for calling kevin')

    return str(resp)


# def send_sms(to_number, from_number):
#     """Using our caller's number and the number they called, send an SMS."""
#     client = Client(ACCOUNT_SID, AUTH_TOKEN)

#     try:
#         client.messages.create(
#             body="There's always money in the banana stand.",
#             from_=from_number,
#             to=to_number
#         )
#     except TwilioRestException as exception:
#         # Check for invalid mobile number error from Twilio
#         if exception.code == 21614:
#             print("Uh oh, looks like this caller can't receive SMS messages.")

if __name__ == "__main__":
    app.run(debug=True)