# 5. Practical Example 1: How does the Python code structure work?

# Python Code Structure Example: Simple Calculator

# This script demonstrates the main components of Python code structure:
# - Importing modules
# - Defining functions for reusable blocks of code
# - Using an entry point with if __name__ == "__main__" to execute code only when run directly

import math  # Import necessary module

# Function definitions for basic operations
def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the division of two numbers."""
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# Main program block
if __name__ == "__main__":
    # Prompt user for operation choice
    print("Select operation: 1) Add 2) Subtract 3) Multiply 4) Divide")
    choice = input("Enter choice (1/2/3/4): ")

    # Take input for numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform chosen operation and print result
    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice")
