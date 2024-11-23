# 16) Write a Python program to separate keys and values from a dictionary using keys() and values() methods.

my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

keys = my_dict.keys()
values = my_dict.values()

print("Keys:", list(keys))
print("Values:", list(values))


# .items() method
l1 = []
l2 = []

for key, vals in my_dict.items():
    l1.append(key)
    l2.append(vals)

print("keys: ", l1)
print("values: ", l2)