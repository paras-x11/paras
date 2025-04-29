# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Question 4:
# Create a class LogWriter that:

# Takes a file path during initialization

# Has a method write_log(message) that appends the message to the file with a timestamp

# Has a method read_logs() that returns all log entries as a list of strings

# class LogWriter:
#     def __init__(self, file_path): ...
#     def write_log(self, message): ...
#     def read_logs(self): ...


# Expected Usage:

# logger = LogWriter("app.log")
# logger.write_log("User logged in")
# logger.write_log("User performed action")

# logs = logger.read_logs()
# print(logs)


# # Output:
# # ["[2025-04-24 14:33:21] User logged in", 
# "[2025-04-24 14:35:02] User performed action"]
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


import os
# os.chdir("D:\\paras\\Assignment\\Python\\Practice\\Test\\Logs")
import datetime

class LogWriter:
    def __init__(self, file_path):
        self._file_path = file_path 
        open(self._file_path, 'a')

    def write_log(self, message):
        timestamp = 

    def read_logs(self):
        pass




logger = LogWriter("D:\\paras\\Assignment\\Python\\Practice\\Test\\Logs\\app.log")
logger.write_log("User logged in")
logger.write_log("User performed action")

logs = logger.read_logs()
print(logs)



