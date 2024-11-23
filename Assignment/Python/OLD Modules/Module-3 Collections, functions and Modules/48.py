# 48. Write a Python function to calculate the factorial of a number (a nonnegative integer) 

number = int(input("Enter number: "))

fact = 1

if number >= 0:
    for i in range(1, number+1):
        fact *= i
    print(fact)
else:
    print("Enter positive number...")



