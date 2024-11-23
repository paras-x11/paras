# 3. Differentiate between append () and extend () methods?

# append() and extend() always add elements to the end of the list.

# Key Differences:
# append() adds the entire object as a single element (even if it's a list, tuple, etc.).
# extend() adds each element from the iterable (e.g., list or tuple) to the list individually.

l1 = [1,2,3,4,5]
l2 = [11,12,13,14,15]

l1.append(l2)
print(l1)
# print(type(l1[5]))

l1.extend(l2) 
print(l1)

# insert() allows you to add an element at a specific position.
l1 = [1,2,3]
l2 = [10,20,30]

l1.insert(1, l2)
print(l1)


