# ### 📌 Loops & Conditionals

# 21. Print a pattern using nested loops.
n = 5
for r in range(1, n+1):
    for c in range(r):
        print("* ", end="")
    print()

for r in range(n, 0, -1):
    for c in range(r):
        print("* ", end="")
    print()

for r in range(1, n+1):
    for s in range(n-r):
        print("  ", end="")
    for c in range(r):
        print("* ", end="")
    print()

for r in range(n, 0, -1):
    for s in range(n-r):
        print("  ", end="")
    for c in range(r):
        print("* ", end="")
    print()
print("==========================")
for r in range(n+1):
    for s in range(n-r):
        print("  ", end="")
    for c in range(2*r+1):
        print("* ", end="")
    print()

for r in range(n, -1, -1):
    for s in range(n-r):
        print("  ", end="")
    for c in range((2*r)+1):
        print("* ", end="")
    print()



# 22. FizzBuzz problem.
# Print the numbers from 1 to n, but for:
# Numbers divisible by 3, print "Fizz" instead of the number.
# Numbers divisible by 5, print "Buzz" instead of the number.
# Numbers divisible by both 3 and 5, print "FizzBuzz" instead of the number.
# For all other numbers, print the number itself.

# try:
#     n = int(input("Enter Range: "))

#     for i in range(1, n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)

# except Exception as e:
#     print(e)




# 23. Check for prime numbers.
# try:
#     n = int(input("Enter Number: "))

#     is_prime = True

#     for i in range(2, n//2):
#         if n % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print(f"{n} is prime")
#     else:
#         print(f"{n} is not prime")
        
# except Exception as e:
#     print(e)



# 24. Print all Armstrong numbers in a range. [1, 153, 370, 371, 407]
# try:
#     num = int(input("Enter Number: "))
#     original_num = num
#     rev = 0

#     cube_total = 0
#     while num > 0:
#         rem = num % 10
#         # rev = rem + rev*10
#         cube_total += (rem**3)
#         num = num // 10
#     print("reversed number: ", rev)
    
#     if original_num == cube_total:
#         print(f"{original_num} is an Armstrong number.")
#     else:
#         print(f"{original_num} is not an Armstrong number.")


# except Exception as e:
#     print(e)


# 25. Create a simple calculator.
class Calc():
    def sum(self, a, b):
        return a + b
    def substraction(self, a, b):
        return a - b
    def multiplication(self, a, b):
        return a * b
    def division(self, a, b):
        return a // b

c = Calc()
try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print("\nEnter 1 for sum - 2 for substraction - 3 for multiplication - 4 for division\n")
    ch = int(input("Enter Your Choice: "))

    if ch == 1:
        print(c.sum(a, b))
    elif ch == 2:
        print(c.substraction(a, b))
    elif ch == 3:
        print(c.multiplication(a, b))
    elif ch == 4:
        print(c.division(a, b))
    else:
        print("Enter valid choice!")
    

except Exception as e:
    print(e)