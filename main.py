from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import demo
import json
import datetime
import pymysql

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""

    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    # if body != None:
    body = body.lower()

    # resp = demo(body)

    # Start our TwiML response
    resp = MessagingResponse()

    # connection = pymysql.connect(host='35.236.23.230',
    #                         user='root',
    #                         password='',
    #                         db='businesses')
    # crsr = connection.cursor()

    # # body = 'subway message hello'
    # splitString = body.split()
    # count = 0
    # businessName = ""
    # for i in splitString:
    #     if i == 'message':
    #         break
    #     if count != 0:
    #         businessName = businessName + ' '
    #     businessName = businessName + i
    #     count = count + 1

    # entry = ("SELECT * FROM data WHERE name='%s'" % businessName)
    # crsr.execute(entry)
    # records = crsr.fetchall()[0]
    # # Uses index[0] because is tuple of tuple
    # # Note: if you are looking at this, GL

    # # print(records[0])

    # # name, phone, email, EId, cal, menu
    # json1_data = json.loads(records[4])
    # datapoints = json1_data
    
    if 'hello' in body:
        msg = "Hello! Thank you for contacting Hooties! How may I assist you today?"
    # if 'menu' in splitString:
    #     msg = "Today's menu is: \n"
    #     msg = msg + records[5]
    # if 'hour' in splitString or 'hours' in splitString: 
    #     if datetime.date in datapoints:
    #         openTime = datapoints[datetime.date][0]
    #         closeTime = datapoints[datetime.date][1]
    #         msg = 'Today\'s hours are ' + openTime + ' to ' + closeTime + '.'
    #     else:
    #         msg = 'We are closed for today.'
    # if 'special' in splitString or 'specials' in splitString:
    #     if datetime.date in datapoints:
    #         specials = datapoints[datetime.date][2]
    #         msg = 'Today\'s specials: ' + specials
    #     else:
    #         msg = 'There are no special\'s today'

    
    elif 'menu' in body:
        msg = "Todays menu is:\n 1. Grilled Pork\n 2. Lemon Chicken\n 3. A5 Wagyu Steak"
    elif 'hours' in body:
        msg = "Todays hours are from 9am to 9pm."
    elif 'specials' in body:
        msg = 'Todays specials are: $2 Tacos'
    elif 'happy hour' in body:
        msg = 'Happy hour is from 1pm to 3pm. The happy hour deal is: buy 1, you buy another'
    else:
        msg = 'Sorry, could you type that more clearly please?'

    resp.message(msg)
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