import os

# Get the current process ID
process_id = os.getpid()
print(f"Current Process ID: {process_id}")

# Get the current user (useful in Unix-like systems)
try:
    current_user = os.getlogin()
    print(f"Current User: {current_user}")
except Exception as e:
    print(f"Could not get login info: {e}")
