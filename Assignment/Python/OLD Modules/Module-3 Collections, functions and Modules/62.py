# 62 Write a Python program to calculate surface volume and area of a cylinder

import math


h = float(input("Enter height: "))
r = float(input("Enter radius: "))

a =  2 * math.pi * r * (h + r)

v = math.pi * r**2 * h

print(f"Area of cylinder is: {a:.2f}")
print(f"volume of cylinder is: {v:.2f}")

