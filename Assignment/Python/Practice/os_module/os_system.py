import os  # Import the os module, which provides functions for interacting with the operating system

# os.system() allows us to send commands to the command line directly from Python
# Whatever command we write inside os.system("...") will be sent to the system's command line
# and executed as if we typed it manually in the terminal (CMD on Windows, terminal on Linux/macOS).

# Example 1: Opening Notepad on Windows
os.system("notepad")  # This command will open Notepad if you’re on Windows, 
                      # just as if you had typed "notepad" in the Command Prompt.

# Example 2: Listing Files
os.system("dir")  # On Windows, this will display a list of files and directories in the current directory.
# Note: On Linux or macOS, replace "dir" with "ls" to achieve the same result
# os.system("ls")

# Example 3: Running Another Python Script
os.system("python another_script.py")  # This will run 'another_script.py' as if you typed 'python another_script.py' 
                                       # directly into the command line. Make sure the script exists in the current directory.

# Note on Usage:
# - os.system() is suitable for simple commands that don't require complex input/output handling.
# - For more advanced cases or when you need better control over input, output, and errors, 
#   consider using subprocess.run(), as it offers more flexibility.

# Summary:
# Using os.system("command") sends "command" to the system's command line exactly as if you had typed it yourself.
# This is useful for simple command-line tasks like opening applications, listing directories, or running other scripts.
