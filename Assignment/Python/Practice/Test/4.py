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

# Output:
# ["[2025-04-24 14:33:21] User logged in", # "[2025-04-24 14:35:02] User performed action"]
# Output:
# ["[2025-04-24 14:33:21] User logged in", # "[2025-04-24 14:35:02] User performed action"]
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


import os
# os.chdir("D:\\paras\\Assignment\\Python\\Practice\\Test\\Logs")
import datetime as dt

# timestamp = dt.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
# print(timestamp)
import datetime as dt

# timestamp = dt.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
# print(timestamp)

class LogWriter:
    def __init__(self, file_path):
        self._file_path = file_path 
        open(self._file_path, 'a').close()
        open(self._file_path, 'a').close()

    def write_log(self, message):
        timestamp = dt.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
        timestamp = timestamp = dt.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
        with open(self._file_path, 'a') as f:
            f.write(f"[{timestamp} {message}],\n")

    def read_logs(self):
        with open(self._file_path, 'r') as f:
            # logs = f.read()                 # this will give one big string
            # return logs
            return [line.strip() for line in f.readlines()]
    
        with open(self._file_path, 'r') as f:
            # logs = f.read()                 # this will give one big string
            # return logs
            return [line.strip() for line in f.readlines()]
    

logger = LogWriter("D:\\paras\\Assignment\\Python\\Practice\\Test\\Logs\\app.log")
logger.write_log("User logged in")
logger.write_log("User performed action 1")
logger.write_log("User performed action 2")

logs = logger.read_logs()
# print(logs)
for log in logs:
    print(log)

today = dt.datetime.now()
 
# Attributes
print("Day: ", today.day)
print("Month: ", today.month)
print("Year: ", today.year)
print("Hour: ", today.hour)
print("Minute: ", today.minute)
print("Second: ", today.second)

