# 32. Write a Python script to sort (ascending and descending) a dictionary by value. 
# The sorted() function in Python is a built-in function that always returns a new sorted list from the items of any iterable (such as a list, tuple, dictionary, etc.). 
# sorted(iterable, key=None, reverse=False)         # by default reverse is false if need reverse make it True


my_dict = {'a': 2, 'b': 3, 'c': 1, 'd': 6, 'e': 5, 'f': 4}

asc = sorted(my_dict.items(), key = lambda x: x[1])                           # x[0] for the key,  x[1] for the value
print("\nAscending by values:",asc)  

asc = sorted(my_dict.items(), key = lambda x: x[1], reverse=True)             # x[0] for the key,  x[1] for the value
print("\nDescending by values:",asc) 