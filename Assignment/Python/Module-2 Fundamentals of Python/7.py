# 7. Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.  

n = int(input("Enter your number: "))

if n == 0:
    print("-> You entered Zero.")

elif n < 0:
    print("-> Enter positive number.")

elif n % 2 == 0:
    print("->", n, "is even number.")

else:
    print("->", n, "is odd number.")