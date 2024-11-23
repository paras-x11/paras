# 33. Write a Python script to concatenate following dictionaries to create a new one.


dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

# Method 1: Using update()
new_dict_update = dict1.copy()
new_dict_update.update(dict2)
new_dict_update.update(dict3)
print("Concatenated dictionary using update():", new_dict_update)

# Method 2: Using unpacking
new_dict_unpacking = {**dict1, **dict2, **dict3}
print("Concatenated dictionary using unpacking:", new_dict_unpacking)

# Method 3: Using | operator
new_dict_operator = dict1 | dict2 | dict3
print("Concatenated dictionary using | operator:", new_dict_operator)


# Manually
new_dict = {}

for key, value in dict1.items():
    new_dict[key] = value

for key, value in dict2.items():
    new_dict[key] = value

for key, value in dict3.items():
    new_dict[key] = value

# new_dict[9] = 'ch'
print("Manually concatenated dictionary:", new_dict)

