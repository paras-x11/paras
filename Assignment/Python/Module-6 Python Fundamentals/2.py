# 3. Write a Python program that demonstrates the correct use of indentation, comments, and variablesfollowing PEP 8 guidelines.

# Program to calculate the area and perimeter of a rectangle based on user input

def calculate_rectangle_properties(length, width):
    """Calculate and return the area and perimeter of a rectangle."""
    area = length * width  # Indented 4 spaces within the function
    perimeter = 2 * (length + width)  # Another line indented within the function
    return area, perimeter

# Take user input for length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Call the function and store the results
area, perimeter = calculate_rectangle_properties(length, width)

# Display the results
print("Area of the rectangle:", area)
print("Perimeter of the rectangle:", perimeter)

print(calculate_rectangle_properties.__doc__)