# 50. Write a Python function to check whether a number is perfect or not. 

# perfect number is its all divisor's sum is number itself : ex. 1 + 2 + 3 = 6, 28, 496, 8128

print("----------------------------------------------------\n")

n = int(input("enter your number: "))
# n=6
divisor = []

for i in range(1, n):
    if n % i == 0:
        divisor.append(i)

if sum(divisor) == n:
    print(f"-> {n} is perfect number.\n")
else:
    print(f"-> {n} is not a perfect number.\n")
    

# checking perfect number between 1 to 10000:
print("----------------------------------------------------\n")
for n in range(1, 10000):
    divisor = []

    for i in range(1, n):
        if n % i == 0:
            divisor.append(i)

    if sum(divisor) == n:
        print(f"{n} is perfect number.")
    else:
        # print(f"{n} is not a perfect number.")
        pass


