# 31. How will you create a dictionary using tuples in python? 

### 1. Using a List of Tuples (Key-Value Pairs)

tuple_list = [('a', 1), ('b', 2), ('c', 3)]
my_dict = dict(tuple_list)
print(my_dict)


### 2. Using Tuples with More Elements

tuple_list = [('a', 'b', 'c'), (1, 2, 3)]
my_dict = {}
for tup in tuple_list:
    my_dict[tup[0]] = tup[1:]  # Use first element as key
print(my_dict)


### 3. Using zip() with Two Lists

keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = dict(zip(keys, values))
print(my_dict)


### 4. Creating Directly from Tuples

my_dict = {('a', 'b'): 1, ('c', 'd'): 2}


