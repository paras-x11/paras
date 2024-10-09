# 9. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.  

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a == b or b == c or a == c:
    print("-> Sum is Zero.")

else:
    sum = a + b + c
    print("->", a, "+", b, "+", c, "=", sum)

