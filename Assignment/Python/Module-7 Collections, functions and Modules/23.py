# 23) Write a Python program to demonstrate the use of functions from the math module. 
import math

# 1. Finding the square root of a number
num = 25
print(f"Square root of {num} is: {math.sqrt(num)}")

# 2. Finding the factorial of a number
num = 5
print(f"Factorial of {num} is: {math.factorial(num)}")

# 3. Calculating the value of pi
print(f"Value of pi is: {math.pi}")

# 4. Finding the sine of an angle (in radians)
angle_rad = math.pi / 2  # 90 degrees in radians
print(f"Sine of 90 degrees (in radians) is: {math.sin(angle_rad)}")

# 5. Finding the cosine of an angle (in radians)
angle_rad = math.pi / 3  # 60 degrees in radians
print(f"Cosine of 60 degrees (in radians) is: {math.cos(angle_rad)}")

# 6. Finding the greatest common divisor of two numbers
num1 = 36
num2 = 60
print(f"GCD of {num1} and {num2} is: {math.gcd(num1, num2)}")

# 7. Rounding a number to the nearest integer
num = 7.8
print(f"{num} rounded to nearest integer is: {round(num)}")

# 8. Getting the absolute value of a number
num = -12
print(f"Absolute value of {num} is: {math.fabs(num)}")

# 9. Finding the power of a number
base = 2
exponent = 3
print(f"{base} raised to the power of {exponent} is: {math.pow(base, exponent)}")

# 10. Getting the logarithm of a number
num = 100
print(f"Natural logarithm of {num} is: {math.log(num)}")
