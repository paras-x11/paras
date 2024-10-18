# 9. Write a Python function that takes two lists and returns true if they have at least one common member. 

def checkList(l1, l2):
    flag = False

    for i in l1:
        if i in l2:
            flag = True
            break
    return flag


l1 = [1,2,3,4,5,6,7]
l2 = [11,12,13,14,15,16,2]

if checkList(l1, l2):
    print("They have common member.")
else:
    print("They don't have common member.")

# print(checkList(l1,l2))


