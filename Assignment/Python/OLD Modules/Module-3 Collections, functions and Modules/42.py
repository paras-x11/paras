# 42. Write a Python program to print all unique values in a dictionary.  

from multiprocessing.reduction import duplicate


def find_unique_values(d1):
    seen = set()
    duplicate_vals = set()

    for val in d1.values():
        if val in seen:
            duplicate_vals.add(val)
        seen.add(val)
    
    unique_val = seen - duplicate_vals
            
    return list(unique_val)

d1 = {'a': 100, 'b': 200, 'C': 100, 'c':300, 'e':500, 'f':700, '+':40, 4:600, 'g':500, 'h':200, 'i':900} 

unique_values = find_unique_values(d1)

print(find_unique_values(d1))

