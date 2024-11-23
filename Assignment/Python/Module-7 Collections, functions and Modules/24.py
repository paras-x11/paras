# 24) Write a Python program to generate random numbers between 1 and 100 using the random module.

import random

# randrange
# randrange(start, stop) generates a random integer from start to stop (excluding stop)
print("randrange example:")
for _ in range(5):
    print("random.randrange(1, 100) ->", random.randrange(1, 100))  # Possible values: 1 to 99

# randrange with step argument
# randrange(start, stop, step) generates a random number from start to stop-1 with a given step
print("\nrandrange with step example:")
for _ in range(5):
    print("random.randrange(1, 100, 2) ->", random.randrange(1, 100, 2))  # Possible values: 1, 3, 5, 7, 9, ..., 99

# Demonstration of randint
# randint(a, b) generates a random integer from a to b (inclusive of both a and b)
print("\nrandint example:")
for _ in range(5):
    print("random.randint(1, 100) ->", random.randint(1, 100))  # Possible values: 1 to 100 (inclusive)
