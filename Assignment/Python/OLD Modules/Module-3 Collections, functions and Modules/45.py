# 45. Write a Python program to find the highest 3 values in a dictionary 

d1 = {'a': 100, 'b': 200, 'c': 300, 'd': 800, 'e': 340, 'f': 250, 'g': 900, }

vals = [num for num in d1.values()]

vals.sort()

print(vals[-3:])

# by Imports the heap queue algorithm library:
import heapq

d1 = {'a': 100, 'b': 200, 'c': 300, 'd': 800, 'e': 340, 'f': 250, 'g': 900}

highest_values = heapq.nlargest(3, d1.values())

print(highest_values)
