# Flow:
# try block: Attempts the operations.
# If an exception occurs:
# The appropriate except block runs.
# The else block is skipped.
# If no exception occurs:
# The else block runs.
# The finally block always executes.


try:
    num = int(input("Enter a number: "))
    result = 10 / num

except ValueError as ve:
    print("Invalid input! Please enter a valid number.")
except ZeroDivisionError as zde:
    print("Division by zero is not allowed.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

else:
    # Execute this block if no exceptions occur
    print(f"else part: The result is: {result}")

finally:
    # Code to execute no matter what (cleanup actions)
    print("Thank you for using our program.")



# Enter a number: <Ctrl+C>
# An unexpected error occurred: KeyboardInterrupt
# Thank you for using our program.

