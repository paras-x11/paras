# 17. Write a Python program to split a list into different variables.


user_input = input("Enter 4 elements separated by spaces: ")
my_list = user_input.split()  

if len(my_list) >= 4:
    a, b, c, d = my_list[:4]
    rest = my_list[4:]  # Store any remaining elements in rest
else:
    print("Error: You need to enter at least 4 elements.")
    exit()

print(f"a: {a}, b: {b}, c: {c}, d: {d}")
if rest:
    print(f"Remaining elements: {rest}")





# dictionary: key as variable
user_input = input("Enter elements separated by spaces: ")
my_list = user_input.split()  

variables = {}

for index, element in enumerate(my_list):
    key = chr(97 + index)  # 97 is the ASCII code for 'a'
    variables[key] = element

print(variables)