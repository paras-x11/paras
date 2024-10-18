# 8. Write a Python program to check a list is empty or not.

def isEmpty(l):
    if len(l) == 0:
        print("List is empty.")
    else:
        print("List is not empty.")
    
    
l = []
l1 = [1,2,3,4,5]

isEmpty(l)
isEmpty(l1)


# --2nd method:
# In Python, empty variables (like lists, strings) are considered False; non-empty ones are True.

if not l:
    print("Null")
else:
    print("Not Null")

if l1 :
    print("Not Null")
else:
    print("Null")


    