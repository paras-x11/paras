# 29. Write a Python program to unzip a list of tuples into individual lists. 

# The zip() function in Python is used to combine multiple iterables (like lists, tuples, or strings) into tuples
# 1. Pairs elements at the same index: It takes the first elements from each iterable and pairs them into a tuple, then takes the second elements, and so on.
# 2. Stops at the shortest iterable: If the iterables have different lengths, zip() stops when the shortest iterable is exhausted.

# The * operator in Python is used to unzip or unpack elements from an iterable, particularly when working with functions like zip()
# Unzipping:
zipped_list = [(1, 'a', True), (2, 'b', False), (3, 'c', True)]

unzipped = zip(*zipped_list)

unzipped_list = list(unzipped)
print(unzipped_list)


# Zipping:
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c']
list3 = [True, False, True, False, True]

unzipped = list(zip(list1,list2,list3))
print(unzipped)


# Unzipping:
l1 = [(1,2,3), (4,5,6), (7,8), ('a','b','c')]

unzipped_lists = list(zip(*l1))
print(unzipped_lists)


# Manually:
l1 = [(1,2,3), (4,5,6), (7,8), ('a','b','c')]
first_list = []
second_list = []
third_list = []

for tup in l1:
    if len(tup) > 0:
        first_list.append(tup[0])  # First element
    else:
        first_list.append(None)      # If empty, append None
        
    if len(tup) > 1:
        second_list.append(tup[1])  # Second element
    else:
        second_list.append(None)
        
    if len(tup) > 2:
        third_list.append(tup[2])   # Third element
    else:
        third_list.append(None)

print()
unzipped_result = [first_list, second_list, third_list]

print(unzipped_result)

for index, lst in enumerate(unzipped_result):
    print(f"List for position {index + 1}: {lst}")





