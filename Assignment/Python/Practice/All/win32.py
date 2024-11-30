import win32api
import win32con # type:ignore

# Display a message box
win32api.MessageBox(
    0,  # Parent window handle (0 means no parent window)
    "Hello, this is a Win32 API message box!",  # Message text
    "Win32 MessageBox",  # Title of the message box
    win32con.MB_OK | win32con.MB_ICONINFORMATION  # Button type and icon
)


# Get the computer name
computer_name = win32api.GetComputerName()

print(f"Computer Name: {computer_name}")


