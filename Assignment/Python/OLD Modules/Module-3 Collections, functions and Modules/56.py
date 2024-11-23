# 56. How will you set the starting value in generating random numbers?


# To set the starting value (seed) for generating random numbers in Python, 
# use the random.seed() function. Setting a seed ensures that the sequence 
# of random numbers generated will be the same each time the program runs.

import random

# Setting the seed
random.seed(10)

# Generating random numbers
# print(random.randint(1, 100))  # Output will be the same every time with seed 10
# print(random.random())         # Output will be the same every time with seed 10



random.seed(10)

# Generate random numbers
for _ in range(10):  # Generate a list of random numbers
    print(random.randint(1, 100))

# -> Predictability: 
#   With the seed set to 10, the output is deterministic. You will get the same sequence every time you run the code with that seed.

# Occurrence of Specific Numbers: 
#   While 9 may not appear in this particular run, if you change the seed or the method of random generation, 
#   you could potentially include 9 in the results. The numbers generated depend on the internal algorithm and its state initialized by the seed.

