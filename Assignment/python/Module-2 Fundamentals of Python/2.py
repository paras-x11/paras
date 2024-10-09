# 2. Write a Python program to get the Factorial number of given number.  

n = int(input("Enter your number: "))
fact = 1

for i in range(1, n+1):
    fact = fact * i
    print(fact)

print("Factorial of", n, "is:", fact)
    