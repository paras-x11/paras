# 41. Write a Python program to combine two dictionary adding values for common keys.  
# d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400}  
# Sample output: Counter ({'a': 400, 'b': 400, ’d’: 400, 'c': 300}). 


def add_values_of_common_keys(d1, d2):
    d3 = {}

    for key, value in d1.items():               # d3 = d1.copy()
        d3[key] = value

    for key, value in d2.items():
        if key in d3:
            d3[key] += value  
        else:
            d3[key] = value   
    
    return d3


d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

new_dict = add_values_of_common_keys(d1, d2)
print("Combined Dictionary:", new_dict)

d1 = {'a': 100, 'b': 200, 'c': 300, 'e': 500, 'f': 700, '+': 40, 4: 600, 'p': 44}
d2 = {'a': 300, 'b': 200, 'd': 400, 'e': 500, 4: 600, '+': 20, 'f': 1300, 'u': 22}

new_dict = add_values_of_common_keys(d1, d2)
print("Combined Dictionary:", new_dict)
