# 16. Write a Python program to check whether a list contains a sub list 
# The sublist in this context refers to a sequence of elements that appear as individual elements in the same order within the main list, 
# not as a single element.



l1 = [1,2,3,4,5,11,12,13,14,15,21,22,23]
l2 = [11,12,13,14,15]
l3 = [11,13,14,15]

def is_sublist(sub_list, main_list):
    sub_list_len = len(sub_list)

    for i in range((len(main_list) - sub_list_len + 1)):
        if main_list[i : (i+sub_list_len)] == sub_list:
            return True
    return False

def is_sublist2(sublist, mainlist):
    s = "".join(map(str, sublist))
    m = "".join(map(str, mainlist))

    # return s in m
    return m.find(s) != -1
         

if is_sublist(l2, l1):
    print("ok")
else:
    print("not ok")

if is_sublist(l3, l1):
    print("ok")
else:
    print("not ok")


