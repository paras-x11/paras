# ### 📌 Lists & Tuples


# 11. Find the second largest element in a list.
# -> sort() modifies the original list and returns None.

elements = [12, 4, 56, 466, 57, 68, 3, 223, 356, 67, 57, 78, 71, 32]
elements.sort(reverse=True)
print(elements)
print(f"second largest element is: {elements[1]}")

# -> sorted() returns a new sorted list without modifying the original list.
elements = [64, 6, 46, 4, 86, 64, 35, 355, 3, 25, 52, 5, 41, 78, 979, 9, 335, 0, 2]

reversed_elements = sorted(elements, reverse=True)
print(elements)
# print(reversed_elements)
print(f"second largest element is: {reversed_elements[1]}")





# 12. Remove duplicates from a list.
# elements = [12, 4, 56, 466, 356, 57, 67, 57, 68, 3, 223, 356, 67, 57, 78, 78, 3]

# unique_elements = []

# for ele in elements:
#     if ele not in unique_elements:
#         unique_elements.append(ele)
# print(elements)
# print(unique_elements)

# 13. Merge two sorted lists into one.
# -> Method 1:
# list1 = [12, 4, 56, 466, 57, 68, 3, 223, 356, 67, 57, 78, 78, 3]
# list2 = [56, 466, 78, 3, 223, 100, 89, 12, 45]

# list1.sort()
# list2.sort()

# merged_list = list1 + list2
# merged_list.sort()

# print(merged_list)

print("\n=============================================================\n")
# -> Method 2:
list1 = [12, 4, 56, 466, 57, 68, 3, 223, 356, 67, 57, 78, 78, 3]
list2 = [56, 466, 78, 3, 223, 100, 89, 12, 45]


list1.sort()
list2.sort()

i=0
j=0
merged_list = [] 

while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        merged_list.append(list1[i])
        i+=1
    else:
        merged_list.append(list2[j])
        j+=1

print(merged_list)
merged_list.extend(list1[i:])
merged_list.extend(list2[j:])
print(merged_list)


# 14. Flatten a nested list.

nested_list = [[1, 2, 3], [4, 5], [6, 7], 8, 9, 10, [11, 12], 13, 14, 15, [16, 17, 18, 19, 20], 21, 22]\

flatten_list = []

for ele in nested_list:
    if isinstance(ele, list):
        flatten_list.extend(ele)
    else:
        flatten_list.append(ele)

print(flatten_list)

print("\n=============================================================\n")

# 15. Find the common elements in two lists.

list1 = [12, 4, 56, 466, 57, 68, 3, 223, 356, 67, 57, 78, 78, 3]
list2 = [56, 466, 78, 3, 223, 100, 89, 12, 45, 22, 67, 34, 90, 33, 4, 356]

common_list = []

for ele in list1:
    if (ele in list2) and (ele not in common_list):
        common_list.append(ele)
print(common_list)

list1 = [10, 20, 30, 40, 50, 60, 70]
list2 = [30, 40, 50, 80, 90, 100]

common_list = []

print("\n=============================================================\n")
for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            if list1[i] not in common_list:
                common_list.append(list1[i])
print(common_list)

print("==============================================")
from functools import reduce

l1 = [10, 20, 30, 40, 50, 60, 70]

sum = reduce(lambda x, y: x + y, l1)
print(sum)
print("==============================================")











# The `isinstance()` function in Python is used to check if an object is an instance of a specific class or a subclass of that class. It returns `True` if the object is an instance of the specified class or subclass, and `False` otherwise.

# ### Syntax:
# isinstance(object, classinfo)

# - **object**: The object you want to check.
# - **classinfo**: A class, type, or a tuple of classes, types, or class-info objects.

# ### Example:

x = 10
print(isinstance(x, int))  # True, because x is an instance of int

y = "Hello"
print(isinstance(y, str))  # True, because y is an instance of str

z = 5.5
print(isinstance(z, (int, float)))  # True, because z is either an int or a float

# ### Explanation:
# - `isinstance(x, int)` returns `True` because `x` is of type `int`.
# - `isinstance(y, str)` returns `True` because `y` is of type `str`.
# - `isinstance(z, (int, float))` checks if `z` is an instance of either `int` or `float`, which is `True` because `z` is of type `float`.

# ---

# ### Other Methods to Check the Type of an Object

# #### 1. **`type()` Function**:
# The `type()` function returns the type of an object. You can use this to directly compare an object's type with a specific class.

x = 10
print(type(x) == int)  # True, because x is of type int

# However, `type()` only checks the exact type and doesn't consider inheritance. This means that it won't return `True` for a subclass.

# #### 2. **`issubclass()` Function**:
# If you want to check whether a class is a subclass of another, you can use the `issubclass()` function.

class Animal:
    pass

class Dog(Animal):
    pass

print(issubclass(Dog, Animal))  # True, because Dog is a subclass of Animal
print(issubclass(Dog, object))  # True, because all classes are subclasses of object

# #### 3. **`hasattr()` Function**:
# You can check if an object has a specific attribute using `hasattr()`. This is useful for checking the existence of attributes or methods before accessing them.

class Car:
    def __init__(self, model):
        self.model = model

car = Car("Toyota")
print(hasattr(car, "model"))  # True, because 'model' is an attribute of car

# #### 4. **`isinstance()` with `type()` Comparison**:
# You can also use `isinstance()` in conjunction with `type()` if you want to check multiple types explicitly.

x = 10
if isinstance(x, int) or isinstance(x, float):
    print("x is a number")

# ---

# ### Summary:

# - **`isinstance()`** is typically preferred because it also works with subclasses.
# - **`type()`** checks the exact type and doesn't account for subclasses.
# - **`issubclass()`** checks if a class is a subclass of another class.
# - **`hasattr()`** is used to check if an object has a particular attribute.

# Let me know if you need more examples or explanations! 😊