# 8. Practical Example 4: How to check the type of a variable dynamically using type().

# Define variables of different types
name = "Alice"          # String
age = 30                # Integer
height = 5.5            # Float
is_student = True       # Boolean
subjects = ["Math", "Science"]  # List
coordinates = (10, 20)  # Tuple
info = {"name": "Alice", "age": 30}  # Dictionary
unique_numbers = {1, 2, 3}  # Set
nothing = None          # NoneType

# Checking and printing the type of each variable
print("Type of 'name':", type(name))
print("Type of 'age':", type(age))
print("Type of 'height':", type(height))
print("Type of 'is_student':", type(is_student))
print("Type of 'subjects':", type(subjects))
print("Type of 'coordinates':", type(coordinates))
print("Type of 'info':", type(info))
print("Type of 'unique_numbers':", type(unique_numbers))
print("Type of 'nothing':", type(nothing))