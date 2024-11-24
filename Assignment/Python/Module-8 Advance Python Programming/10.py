# 10) Write a Python program to print custom exceptions.

# Define a custom exception
class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

# Function that raises the custom exception
def check_number(number):
    if number < 0:
        raise CustomException(f"Negative numbers are not allowed: {number}")
    elif number == 0:
        raise CustomException("Zero is not a valid input.")
    else:
        print(f"Valid number: {number}")

# Main program to demonstrate custom exceptions
try:
    num = int(input("Enter a number: "))
    check_number(num)
except CustomException as e:
    print(f"Custom Exception Caught: {e}")
except ValueError as ve:
    print("Invalid input! Please enter a valid number.\n->", ve)
