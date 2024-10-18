import random

# Generate random numbers
print("Random float between 0 and 1:", random.random())
print("Random integer between 1 and 10:", random.randint(1, 10))
print("Random float between 1 and 10:", random.uniform(1, 10))

# List operations
fruits = ['apple', 'banana', 'cherry', 'papaya','water melon']
print("Random fruit:", random.choice(fruits))

random.shuffle(fruits)
print("Shuffled fruits:", fruits)

print("Two random fruits (allow duplicates):", random.choices(fruits, k=10))
print("Two unique random fruits (unique element):", random.sample(fruits, k=5))