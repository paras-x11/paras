# 2. How will you remove last object from a list?
# Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]? 

list1 = [2, 33, 222, 14, 25]

print("list1[-1] will return the last element of list:", list1[-1])

print("\nYour list is:", list1)

print("\ndeleting last item using del keyword: ")
del list1[-1]
print(list1)

print("\ndelete last item using pop: ")
list1.pop()
print(list1)


