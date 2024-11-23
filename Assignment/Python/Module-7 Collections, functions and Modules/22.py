# 22) Write a Python program to create a lambda function with two expressions.

# Creating a lambda function with two expressions. (Example: multiply and add 2)
# Since lambda functions only support a single expression, we can combine expressions with a tuple or other structure.

operation = lambda x, y: (x + y, x * y)  # Returns a tuple with sum and multiply

result = operation(3, 4)
print("Sum and multiply:", result)
