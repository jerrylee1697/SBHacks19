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

    # resp = demo(body)

    # Start our TwiML response
    resp = MessagingResponse()

    # if 'hello' in body:
    #     msg = "Hello! Thank you for contacting Hooties! How may I assist you today?"
    # elif 'menu' in body:
    #     msg = "Todays menu is:\n 1. Raw Pork\n 2. Raw Chicken\n 3. Well Done A5 Wagyu"
    # elif 'hours' in body:
    #     msg = "Todays hours are from 9am to 9pm."
    # elif 'specials' in body:
    #     msg = 'Todays specials are: $5 Tacos'
    # elif 'happy hour' in body:
    #     msg = 'Happy hour is from 1pm to 3pm. The happy hour deal is: buy 1, you buy another'
    # else:
    #     msg = 'Sorry, could you type that more clearly please?'

    resp.message(demo(body))
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