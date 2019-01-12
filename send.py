# Download the helper library from https://www.twilio.com/docs/python/install
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACb6e8daffa9eade3ea0033124b181838c'
auth_token = 'd1c8e2c0c62c519925820e6be3d190ae'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="I'm only allergic to bitches. And I'm sneezin",
                     from_='+15624541318',
                     media_url='https://demo.twilio.com/owl.png',
                     to='+16262786801'
                 )

print(message.sid)