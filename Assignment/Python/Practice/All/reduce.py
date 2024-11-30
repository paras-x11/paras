from functools import reduce

# Example 1: Using reduce with a two-argument function
# This works because reduce expects a two-argument function
# Here, we sum all elements in a list
numbers = [1, 2, 3, 4, 5]

# reduce applies the lambda function cumulatively
# First: (1 + 2) -> Result is 3
# Next: (3 + 3) -> Result is 6
# Next: (6 + 4) -> Result is 10
# Finally: (10 + 5) -> Result is 15
sum_result = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", sum_result)  # Output: 15

# Example 2: Trying to use reduce with a one-argument function
# This will cause an error because reduce expects a function with two arguments
try:
    # Here, we define a function that takes only one argument
    single_arg_function = lambda x: x * 2
    # This will raise an error
    reduce(single_arg_function, numbers)
except TypeError as e:
    print("Error with one-argument function:", e)

# Example 3: Trying to use reduce with a three-argument function
# This will also cause an error because reduce cannot handle functions with more than two arguments
try:
    # Define a three-argument function
    three_arg_function = lambda x, y, z: x + y + z
    # Attempt to use it with reduce, which will raise an error
    reduce(three_arg_function, numbers)
except TypeError as e:
    print("Error with three-argument function:", e)

# Explanation:
# - reduce requires a function that takes exactly two arguments.
# - It uses the first two items in the iterable with the function, then applies the function
#   cumulatively between the result and each subsequent item.
# - A function with one argument cannot handle two inputs, and a function with three arguments
#   will have extra, unused parameters, which causes a TypeError.