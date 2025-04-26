# 📌 Basic Syntax & Variables:

# Write a program to swap two variables.

# a = 5
# b = 6
# print(f"a = {a}, b = {b}")


# a = a + b
# b = a - b
# a = a - b
# print(f"a = {a}, b = {b}")


# a, b = b, a
# print(f"a = {a}, b = {b}")


# Check if a number is even or odd.

# n = input("Enter Number: ")
# try:
#     if int(n) % 2 == 0:
#         print(f"{n} is even number")
#     else:
#         print(f"{n} is odd number")
# except ValueError as ve:
#     print("Enter Number only")
    

# Find the largest among 3 numbers.
# try:
#     a = int(input("Enter a: "))
#     b = int(input("Enter b: "))
#     c = int(input("Enter c: "))

#     if a > b and a > c:
#         print(f"{a} is greatest")

#     elif b > a and b > c:
#         print(f"{b} is greatest")
#     else:
#         print(f"{c} is greatest")


# except ValueError as ve:
#     print("-> Invalid Input!")


# Take user input and reverse it.
# text = input("Enter Text: ")
# reversed_text = text[::-1]
# print(reversed_text)

# Calculate area and perimeter of a rectangle/circle.

# try:
#     l = int(input("Enter rectangle length: "))
#     w = int(input("Enter rectangle width: "))

#     print(f"Perimeter of rectangle: {(l*w)}")
#     print(f"Area of rectangle: {2*(l+w)}")
    
# except Exception as e:
#     print(e)

import math
try:
    r = int(input("Enter circle radius: "))

    print(f"Perimeter of rectangle: {(2*math.pi*r):.2f}")
    print(f"Area of rectangle: {math.pi*(r**2):.2f}")

except Exception as e:
    print(e)



