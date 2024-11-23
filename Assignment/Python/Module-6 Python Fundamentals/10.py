# 1. Write a Python program to apply the map() function to square a list of numbers.
numbers = [1, 2, 3, 4, 5]
def square(x):
    return x * x
squared_numbers = list(map(square, numbers))
print(squared_numbers)

# 2. Write a Python program that uses reduce() to find the product of a list of numbers.
from functools import reduce
numbers = [1, 2, 3, 4, 5]
def multiply(x, y):
    return x * y 
product = reduce(multiply, numbers)
print(product)

# 3. Write a Python program that filters out even numbers using the filter() function.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def is_odd(x):
    return x % 2 != 0
odd_numbers = list(filter(lambda x : x % 2 != 0, numbers))
print(odd_numbers)
