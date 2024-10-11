import pywhatkit as kit # type: ignore
import time

# Define the phone number (including country code)
phone_number = '+919023495462'  # Replace with the actual phone number

# Define the message you want to send
message = 'Hello! '

# Number of messages to send
num_messages = 5  # Change this to the number of messages you want to send
interval = 0

0  # Interval between messages in seconds

for i in range(num_messages):
    # Send the message instantly
    # True to wait for confirmation
    kit.sendwhatmsg_instantly(phone_number, message, 15, True)

    print(f"Message {i + 1} sent to {phone_number}: '{message}'")

    time.sleep(interval)  # Wait for 10 seconds before sending the next message
