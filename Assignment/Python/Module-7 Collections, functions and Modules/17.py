# 17) Write a Python program to convert two lists into one dictionary using a for loop.

keys = ['a', 'b', 'c']
values = [1, 2, 3]

my_dict = {}
for i in range(len(keys)):
    my_dict[keys[i]] = values[i]

print("Dictionary from lists:", my_dict)



keys = ['a', 'b', 'c', 'd', 'e', 'f']
values = [1, 2, 3, 4, 5, 6, 7]

my_dict2 = {}

for key, vals in (zip(keys, values)):
    my_dict2[key] = vals

print(my_dict2)



result_dict = dict(zip(keys, values))
print(result_dict)