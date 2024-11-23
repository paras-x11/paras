# 40. Write a Python program to map two lists into a dictionary  


def make_dict_from_2_list(l1, l2):
    dict1 = {}

    if len(l1) == len(l2):
        for i in range(len(l1)):
            dict1.update({ l1[i] : l2[i]})
        # dict1 = {l1[i]: l2[i] for i in range(len(l1))}
    else:
        print("list len is not same")
    return dict1


l1 = ['a', 'b', 'c', 'd']
l2 = [1, 2, 3, 4]

my_dict = make_dict_from_2_list(l1, l2)
print(my_dict)


keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]

mapped_dict = {}

for index, key in enumerate(keys):
    mapped_dict[key] = values[index]

print("Mapped Dictionary (Using enumerate):", mapped_dict)


keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]

# Method 1: Using dictionary comprehension: coprehension means creating new
mapped_dict_comprehension = {key: value for key, value in zip(keys, values)}

# Method 2: Using the dict() constructor
mapped_dict_constructor = dict(zip(keys, values))

print("Mapped Dictionary (Using Comprehension):", mapped_dict_comprehension)
print("Mapped Dictionary (Using dict constructor):", mapped_dict_constructor)
