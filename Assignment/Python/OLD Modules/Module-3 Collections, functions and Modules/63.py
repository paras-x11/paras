# 63. Write a Python program to returns sum of all divisors of a number 


n = int(input("Enter number: "))

d = []

for i in range(1, n+1):
    if n % i == 0:
        d.append(i)

print("all divisor of", n, "is:", d)