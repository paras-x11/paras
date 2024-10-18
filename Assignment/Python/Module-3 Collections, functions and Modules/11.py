# 11. Write a Python function that takes a list and returns a new list with unique elements of the first list.  

def removeDuplicate(l1):
    return list(set(l1))

l1 = [1,2,3,4,4,3,2,2,2,3,4,55,6,6,6,6,6,54,34]

new_list = removeDuplicate(l1)

print(new_list)


