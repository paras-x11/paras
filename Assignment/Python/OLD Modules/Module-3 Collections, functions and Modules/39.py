# 39. Write a Python script to merge two Python dictionaries  


dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# Method 1: Using update()
new_dict_update = dict1.copy()
new_dict_update.update(dict2)
print("Concatenated dictionary using update():", new_dict_update)

# Method 2: Using unpacking
new_dict_unpacking = {**dict1, **dict2}
print("Concatenated dictionary using unpacking:", new_dict_unpacking)

# Method 3: Using | operator
new_dict_operator = dict1 | dict2 
print("Concatenated dictionary using | operator:", new_dict_operator)


# Manually
new_dict = {}

for key, value in dict1.items():
    new_dict[key] = value

for key, value in dict2.items():
    new_dict[key] = value


# new_dict[9] = 'ch'
print("Manually concatenated dictionary:", new_dict)
