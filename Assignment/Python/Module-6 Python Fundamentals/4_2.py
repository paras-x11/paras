# 10. Practical Example 6: Write a Python program to check if a number is prime using if_else.

n = int(input("Enter number: "))

flag = True

for i in range (2, n):
    # print(i)
    if n % i == 0:
        flag = False
        break

if flag == True:
    print(f"{n} is Prime")

if flag == False:
    print(f"{n} is Not a Prime")


# List prime numbers up to a given limit

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

limit = int(input("Enter the limit: "))

print(f"Prime numbers up to {limit}:")
for num in range(2, limit + 1):
    if is_prime(num):
        print(num, end=" ")
