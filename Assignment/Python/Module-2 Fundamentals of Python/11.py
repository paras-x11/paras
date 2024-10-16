# 11. Write a python program to sum of the first n positive integers. 

n = int(input("Enter number: "))
sum = 0

for i in range(1, n+1):
    sum = sum + i

print("-> Sum of", n, "natural numbers: ", sum)
