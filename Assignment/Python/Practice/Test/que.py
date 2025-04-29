# Question 1:
# Write a function that takes a nested list and returns a flattened version of it.

# # Input: [1, [2, [3, 4], 5], 6]
# # Output: [1, 2, 3, 4, 5, 6]


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Question 2:
# Given a dictionary where keys follow the format "group_item", group all values by the group part.


# # Input:
# data = {
#     "fruits_apple": 10,
#     "fruits_banana": 5,
#     "veggies_carrot": 7,
#     "fruits_orange": 8,
#     "veggies_broccoli": 4,
# }

# # Output:
# # {
# #     "fruits": {"apple": 10, "banana": 5, "orange": 8},
# #     "veggies": {"carrot": 7, "broccoli": 4}
# # }

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Question 3:
# Create a base class Employee with a method get_salary().
# Then create a subclass Manager that extends this method to include a bonus.

# class Employee:
#     def __init__(self, name, salary): ...
#     def get_salary(self): ...

# class Manager(Employee):
#     def __init__(self, name, salary, bonus): ...
#     def get_salary(self):  # override and include bonus


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


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