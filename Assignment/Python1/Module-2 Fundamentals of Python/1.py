# 1. Write a Python program to check if a number is positive, negative or zero.  

a = int(input("Enter Your Number: "))

if a == 0 :
    print("You entered zero: ", a)

elif a > 0:
    print("You entered positive number:", a)

else :
    print("You entered negative number:", a)