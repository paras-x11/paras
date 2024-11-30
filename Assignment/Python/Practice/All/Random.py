import random

# Generate random numbers
print("Random float between 0 and 1:", random.random())  # Random float in [0.0, 1.0)
print("Random integer between 1 and 10:", random.randint(1, 10))  # Random int in [1, 10] inclusive
print("Random float between 1 and 10:", random.uniform(1, 10))  # Random float in [1.0, 10.0]

# List operations
fruits = ['apple', 'banana', 'cherry', 'papaya', 'watermelon']
print("Random fruit:", random.choice(fruits))  # Random single item from list

random.shuffle(fruits)  # Shuffles the list in place
print("Shuffled fruits:", fruits)

print("Two random fruits (allow duplicates):", random.choices(fruits, k=2))  # Random sample with replacement
print("Five unique random fruits (no duplicates):", random.sample(fruits, k=5))  # Unique random sample

# Generate a random number within a specific range, with a given step
print("Random number from 0 to 100 with step of 5:", random.randrange(0, 101, 5))  # Possible values: 0, 5, 10, ..., 100

# Set a seed for reproducibility (same random sequence each run)
random.seed(42)
print("Random number with seed 42:", random.randint(1, 100))

# Reset the random seed to get a new sequence
random.seed(None)
print("Random number without seed:", random.randint(1, 100))

