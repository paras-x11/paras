# 5. How will you compare two lists?



list1 = [1, 2, 3, 5, 4, 3]      
list2 = [1, 3, 2, 3, 5, 4]      


print(id(list1), id(list2))                         # Lists are mutable, so they have different memory locations

if list1 is list2:                                  # The 'is' keyword checks if both lists reference the same object in memory.
    print("Equal (using is)")
else:
    print("Not equal (using is)")                   # always this part executed.


if list1 == list2:                                  # The '==' checks if the values in both lists are equal.
    print("Equal (using ==)")
else:
    print("Not equal (using ==)")


# if elements are same but not in order:
if sorted(list1) == sorted(list2):                                  
    print("Equal (after sorting)")
else: 
    print("Not equal (after sorting)")

