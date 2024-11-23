# 27. Write a Python program to find the repeated items of a tuple. 



tup = (1, 2, 3, 4, 5, 1, 3, 5, 6, 7, 6, 5, 4, 3, 5, 7, 8, 9, 0)

# Initialize an empty set to track seen items and a list for repeats
seen = set()
repeated_items = []

for ele in tup:
    if ele in seen:
        if ele not in repeated_items:
            repeated_items.append(ele)
    else:
        seen.add(ele)

print("Repeated items:", repeated_items)




