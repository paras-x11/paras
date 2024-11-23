# 53. How can you pick a random item from a list or tuple? 

l = [num for num in range(1, 50) if num % 2 == 0]

t = (12,3,4,5,6,6,77,'gt',65,5,54,4,3,'3','de')
print(t)
import random

random_from_list = random.choice(l)
random_from_tuple = random.choice(t)

print("random item from list:", random_from_list)
print("random item from tuple:", random_from_tuple)