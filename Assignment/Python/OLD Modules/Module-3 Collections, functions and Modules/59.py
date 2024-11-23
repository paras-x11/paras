# 59. Write a Python program to convert degree to radian 



import math


degree = float(input("Enter Degree: "))

r = degree * (math.pi / 180)

print(f"radian is: {r:.2f}")
