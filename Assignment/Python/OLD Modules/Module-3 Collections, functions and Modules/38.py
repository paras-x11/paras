# 38. Write a Python program to check multiple keys exists in a dictionary  

def check_keys_in_dict(my_dict, keys_to_check):
    flag = True

    for key in keys_to_check:
        if key not in my_dict:
            flag = False
            break

    if flag:
        print("yes all keys in dict1.")
    else:
        print("some keys are missing")


dict1 = {
    'a' : 1, 'b': 2, 'c' : 3, 'd': 4, 'e' : 5, 'f': 6, 'g' : 7, 'h': 8,
}

l1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
l2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i']
l3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

check_keys_in_dict(dict1, l1)
check_keys_in_dict(dict1, l2)
check_keys_in_dict(dict1, l3)


