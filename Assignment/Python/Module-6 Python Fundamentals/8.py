# Practical Example: 1) Write a Python program to skip 'banana' in a list using the continue statement. List1 = ['apple', 'banana', 'mango']

List1 = ['apple', 'banana', 'mango']

for ele in List1:
    if ele == 'banana':
        continue
    print(ele)


# Practical Example: 2) Write a Python program to stop the loop once 'banana' is found using the break statement

List1 = ['apple', 'banana', 'mango']

for ele in List1:
    if ele == 'banana':
        break
    print(ele)
