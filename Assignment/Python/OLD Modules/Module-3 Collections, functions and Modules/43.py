# 43. Why Do You Use the Zip () Method in Python?  


# The `zip()` function in Python combines multiple iterables (like lists or tuples) into tuples based on their corresponding positions. Here are some key points:

# -> Uses of `zip()`

# 1. Combine Lists:
names = ['Alice', 'Bob']
scores = [85, 90]
combined = list(zip(names, scores))  # [('Alice', 85), ('Bob', 90)]

# -> 2. Create Dictionaries:

keys = ['name', 'age']
values = ['Alice', 30]
my_dict = dict(zip(keys, values))  # {'name': 'Alice', 'age': 30}

# 3. Iterate Simultaneously:
for num, char in zip([1, 2], ['a', 'b']):
    print(num, char)  # Outputs: 1 a  \n 2 b

#4. Unzip Tuples:
zipped = [('Alice', 85), ('Bob', 90)]
names, scores = zip(*zipped)  # names: ('Alice', 'Bob'), scores: (85, 90)

# 5. Handle Different Lengths:
# If the input iterables are of different lengths, `zip()` stops at the shortest one.
list1 = [1, 2, 3]
list2 = ['a', 'b']
combined = list(zip(list1, list2))  # [(1, 'a'), (2, 'b')]

### Summary
# The `zip()` function makes it easy to pair elements from multiple iterables, create dictionaries, and iterate through data efficiently.