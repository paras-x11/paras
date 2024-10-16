# 3. Write a Python program to get the Fibonacci series of given range.  

n = int(input("Enter how many numbers u want in fibonacci series: "))

a = 0
b = 1

for i in range(n):
    if i == 0:
        print(0, end=", ")

    elif i == 1:
        print(1, end=", ")

    else:
        c = a + b
        a = b
        b = c
        print(c, end=", ")
    