# 30. Write a Python program to convert a list of tuples into a dictionary. 



l1 = [('a','b','c'), (1,2,3), ('d',4,5,6)]

main_dict = {}
temp = {}


for index, ele in enumerate(l1):
    temp.update({index : ele})
    main_dict.update(temp)

print(main_dict)

# Using dictionary comprehension to create the dictionary
# main_dict = {index: ele for index, ele in enumerate(l1)}



# ----------- #
# if tuple is of 2 Elements:

li = [("a", 1), ("b", 2), ("c", 3)]
result = dict(li)
print(result)



