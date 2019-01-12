from twilio.twiml.messaging_response import MessagingResponse

def demo(body):
    resp = MessagingResponse()
    if 'hello' in body:
        msg = "Hello! Thank you for contacting Hooties! How may I assist you today?"
    elif 'menu' in body:
        msg = "Todays menu is:\n 1. Raw Pork\n 2. Raw Chicken\n 3. Well Done A5 Wagyu"
    elif 'hours' in body:
        msg = "Todays hours are from 9am to 9pm."
    elif 'specials' in body:
        msg = 'Todays specials are: $5 Tacos'
    elif 'happy hour' in body:
        msg = 'Happy hour is from 1pm to 3pm. The happy hour deal is: buy 1, you buy another'
    return resp.message(msg)