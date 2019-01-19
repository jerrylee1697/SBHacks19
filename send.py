# Download the helper library from https://www.twilio.com/docs/python/install
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = '###ACCOUNT_SID###'
auth_token = '###Token###'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="I'm only allergic to bitches. And I'm sneezin",
                     from_='+16261234567',
                     media_url='https://demo.twilio.com/owl.png',
                     to='+16261234567'
                 )

print(message.sid)