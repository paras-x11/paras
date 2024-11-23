# Iterator: A general object that can be looped over, defined by __iter__() and __next__().
# Generator: A type of iterator created with a function that uses yield, automatically handling iteration and state management.# Key Concepts:


# - range() is an iterator in Python 3, not a generator. It generates values lazily.
# - A generator is a function that uses `yield` to return values lazily, one at a time.

# Example 1: Using range() as an iterator
print("Using range() as an iterator:")
for num in range(5):  # range(5) generates numbers from 0 to 4 lazily
    print(num)  # Outputs: 0, 1, 2, 3, 4

# Example 2: Using a generator
def my_generator(start, end):
    while start < end:
        yield start  # Yield values lazily one at a time
        start += 1

print("\nUsing my_generator() as a generator:")
gen = my_generator(0, 5)  # Create a generator object
for value in gen:
    print(value)  # Outputs: 0, 1, 2, 3, 4

# Explanation:
# - range() is an iterator that generates values lazily, but it is not a generator.
# - my_generator() is a true generator function that uses `yield` to produce values lazily.

#  range() is an example of a built-in iterator, and now you’re asking for examples of built-in generators in Python.

# Here are a few examples of built-in generator-like functions in Python:

# 1. enumerate():
# enumerate() is a built-in generator function that adds a counter to an iterable and returns it as an iterator.

# Example: Using enumerate() as a generator-like iterator
items = ['apple', 'banana', 'cherry']
for index, item in enumerate(items):
    print(index, item)
    
# enumerate() is a generator that produces pairs of index and value lazily, as you iterate over the iterable.
