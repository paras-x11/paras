# 1. What is List? How will you reverse a list? 

# What is a List?

# A list in Python is a data structure used to store multiple items in a single variable (e.g., integers, strings).
# It is ordered, mutable, and can contain elements of different data types. 
# You can access items using an index and modify the list by adding, removing, or changing elements.

# Key points:
# Ordered: Items have a fixed order.
# Mutable: Can be modified.
# Dynamic: Can grow or shrink in size.

 
# You can reverse a list in Python using several methods:

# 1. Using `reverse()` Method (in-place):
my_list = [1, 2, 3, 4]
my_list.reverse()   # Modifies the list in place
print(my_list)      # Output: [4, 3, 2, 1]


# 2. Using Slicing (creates a new list):
my_list = [1, 2, 3, 4]
reversed_list = my_list[::-1]  # Creates a reversed copy
print(reversed_list)           # Output: [4, 3, 2, 1]


# 3. Using `reversed()` Function (returns an iterator):
my_list = [1, 2, 3, 4]
reversed_list = list(reversed(my_list))  # Converts iterator to list
print(reversed_list)                     # Output: [4, 3, 2, 1]




