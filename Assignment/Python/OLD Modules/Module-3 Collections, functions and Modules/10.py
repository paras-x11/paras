# 10. Write a Python program to generate and print a list of first and last 5 elements where the values are
# square of numbers between 1 and 30. 

l1 = []
l2 = []

for i in range(1,31):
    l1.append(i**2)

print(f"List1:{l1}")

l2.extend(l1[:5] + l1[-5:])
print(l2)


