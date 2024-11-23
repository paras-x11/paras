# 22. Write a Python program to check whether an element exists within a tuple. 

tup = (22,24,26,27,29)

ele = int(input("Enter(21 to 30): "))

if ele in tup:
    print(f"{ele} is exist in tuple")
else:
    print(f"{ele} is not exist in tuple")

