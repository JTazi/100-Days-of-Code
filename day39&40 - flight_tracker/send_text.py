# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 11:30:10 2024

@author: jtazioli
"""
from twilio.rest import Client


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
TWILIO_ACCOUNT_SID= 'ACf44a479df235aa0fe1864c1ea9e212e3'
TWILIO_AUTH_TOKEN= 'd9f5b036f609f236680ebaf5a1aadbd0'

# account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
# auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_text(msg_lst):
    for msg in msg_lst:
        message = client.messages.create(
          from_='+18446451052',
          body=msg,
          to='+12244226472'
        )