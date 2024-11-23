# 13. Write a Python program to select an item randomly from a list. 

import random

l1 = ['apple','banana','water melon','papaya','mango']

print(random.choice(l1),"\n")

# with index number
length = len(l1)
choice = random.randint(0, length-1)           #randit is inclusive means (0,2) it will generate 0,1 & 2 randomly
print(f"{choice} : {l1[choice]}")



