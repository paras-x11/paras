# 60. Write a Python program to calculate the area of a trapezoid 

b1 = float(input("Enter base 1: "))
b2 = float(input("Enter base 2: "))

h = float(input("Enter height: "))


area = (b1 + b2) * h / 2

print(f"Area of Trapezoid is: {area:.2f}")