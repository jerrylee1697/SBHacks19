from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import demo

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""

    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    body = body.lower()

    resp = demo()

    # Start our TwiML response
    # resp = MessagingResponse()

    # # Determine the right reply for this message
    # if 'hello' in body:
    #     resp.message("You're a ho!")
    # elif 'bye' in body:
    #     resp.message("Bye bitch!")

    # Add a message
    # resp.message("The Robots are coming! Head for the hills!")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)