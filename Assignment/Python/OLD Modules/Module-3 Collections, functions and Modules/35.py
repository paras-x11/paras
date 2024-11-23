# 35.How Do You Traverse Through A Dictionary Object In Python?

# To traverse a dictionary in Python, you can use a `for` loop in several different ways, depending on whether you want to access keys, values, or both. Here are the main methods:

### 1. Traversing Keys Only
# To loop through only the keys in the dictionary:

my_dict = {'a': 1, 'b': 2, 'c': 3}

for key in my_dict:
    print(key)


### 2. Traversing Values Only
# To loop through only the values in the dictionary:

for value in my_dict.values():
    print(value)


### 3. Traversing Keys and Values Together
# To loop through both keys and values:

for key, value in my_dict.items():
    print(f"{key}: {value}")


# Each method can be used as needed depending on whether you require keys, values, or both.