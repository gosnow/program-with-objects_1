# from twilio.rest import TwilioRestClient
# Your Account Sid and Auth Token from twilio.com/user/account
from twilio import rest
account_sid = "ACe9596fc15143af79e4c810b6f901f4a3"
auth_token = "85b212b907947f5f2845ae9d85655556"
client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hi Geo",
	to="+19259517677", # Replace with your phone number
	from_="+19253095975") # Replace with your Twilio number
print message.sid
# SM1f0b961d798f4d72811ab82ea67e50e7
