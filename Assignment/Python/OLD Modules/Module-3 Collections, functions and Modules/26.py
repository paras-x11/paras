# 26. Write a Python program to replace last value of tuples in a list. 

l1 = [(1,2,3), (4,5,6), (7,8), (9,10)]
# print(l1[0][:-1]+(100,))
new_value = 0

def replace_last_values(li):
    modified_list = []

    for tup in li:
        temp_list = list(tup)

        temp_list[-1] = new_value

        temp_list = tuple(temp_list)
        modified_list.append(temp_list)
    
    print(modified_list)

replace_last_values(l1)







