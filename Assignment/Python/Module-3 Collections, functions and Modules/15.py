# 15. Write a Python program to get unique values from a list


def get_Unique_Values(l):
    new_list = []
    for values in l:
        if values not in new_list:
            new_list.append(values)
    
    print(new_list)


l1 = [1,2,34,5,5,66,3,2,56,7,66]

# l1 = [set(l1)]                    # This will create a list containing one set
l1 = list(set(l1))                  # This converts l1 into a set to remove duplicates and then converts that set back into a list
print(l1)


l2 = [55,6,4,4,2,2,90,4,5,6,78,55,22]
get_Unique_Values(l2)