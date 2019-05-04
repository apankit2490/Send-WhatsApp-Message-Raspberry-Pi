from twilio.rest import Client
#from fetch_location.py import *

# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
client = Client()

# this is the Twilio sandbox testing number
from_whatsapp_number='whatsapp:+14155238886'
# replace this number with your own WhatsApp Messaging number
to_whatsapp_number='whatsapp:+919686280812'

map_links=''
with open('location_log.txt','r') as file:
    for data in file:
        map_links+=file.readline()

message='Garbage found! There was solid waste located at '+str(map_links)+'You are requested to take the necessary action.'
client.messages.create(body=message,
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)