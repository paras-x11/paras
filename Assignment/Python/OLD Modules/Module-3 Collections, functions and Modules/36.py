# 36. How Do You Check The Presence Of A Key In A Dictionary? 

# To check if a key is present in a dictionary, you can use the `in` keyword:

my_dict = {'a': 1, 'b': 2, 'c': 3}

if 'a' in my_dict:
    print("Key 'a' is present.")
else:
    print("Key 'a' is not present.")

# Or use the `get` method, which returns `None` if the key isn’t found:

if my_dict.get('a') is not None:
    print("Key 'a' is present.")
else:
    print("Key 'a' is not present.")
