# 15) Write a Python program to update a value at a particular key in a dictionary.

my_dict = {'a': 1, 'b': 2, 'c': 3}

my_dict['b'] = 5

print("Updated Dictionary:", my_dict)




my_dict = {'a': 1, 'b': 2, 'c': 3}

key = input("Enter the key to update: ")
new_value = int(input("Enter the new value: "))

if key in my_dict:
    my_dict[key] = new_value
    print("Updated Dictionary:", my_dict)
else:
    print(f"Key '{key}' not found in the dictionary.")







