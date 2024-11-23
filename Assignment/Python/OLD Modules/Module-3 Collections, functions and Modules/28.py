# 28. Write a Python program to remove an empty tuple(s) from a list of tuples. 


l1 = [(1,2,3), (4,5,6), (), (7,8), (7,7,7), (), (9,10), (), (5,), ("c",), (9,2,6), (), (6,1,9)]

def remove_empty_tuple(li):

    for index, tup in enumerate(li):
        if not tup:
            li.pop(index)

    print(li)

remove_empty_tuple(l1)



