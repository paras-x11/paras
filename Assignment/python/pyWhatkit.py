import pywhatkit as kit
import datetime

# Define the phone number (including country code)
phone_number = '+919023495462'  # Replace with the actual phone number

# Define the message you want to send
message = 'Hello! This is a test message from PyWhatKit.'


# Get the current time and set a delay for sending the message
now = datetime.datetime.now()
hour = now.hour
minute = now.minute + 2  # Send the message 2 minutes from now

# Send the message
kit.sendwhatmsg(phone_number, message, hour, minute)

print(f"Message sent to {phone_number}: '{message}'")
