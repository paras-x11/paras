# 52. How Many Basic Types Of Functions Are Available In Python? 


# 1. Built-in Functions
# Functions that are already part of Python, like print(), len(), and type().

# 2. User-Defined Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Paras"))

# 3. Anonymous (Lambda) Functions
add = lambda x, y: x + y
print(add(3, 5))  

# 4. Recursive Functions
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  

# These four types cover the main ways functions are used in Python.