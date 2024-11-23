# 7. Practical Example 3: How to take user input using the input() function.

# Taking different types of inputs from the user

# String input
name = input("Enter your name: ")
print("Hello, " + name + "!")

# Integer input
age = int(input("Enter your age: "))  # Convert input to integer
print("Your age is:", age)

# Float input
height = float(input("Enter your height in meters: "))  # Convert input to float
print("Your height is:", height, "meters")

# Boolean input (converting string input to boolean)
is_student_input = input("Are you a student? (yes/no): ").strip().lower()
is_student = is_student_input == "yes"
print("Is student:", is_student)
