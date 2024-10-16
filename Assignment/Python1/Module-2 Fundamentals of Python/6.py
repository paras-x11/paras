# 6. Write python program that swap two number with temp variable and without temp variable.  

a = 10
b = 20

print("\na =", a, "b =", b)

print("\nSwapping variables with temp: ")

temp = a
a = b
b = temp

print("a =", a, "b =", b)

#------------------------------------------------------------------#

a = 10
b = 20

print("\nSwapping variables without temp: ")

a = a + b   #a = 10+20 = 30
b = a - b   #b = 30-20 = 10
a = a - b

print("a =", a, "b =", b)


