# 44. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.  
# Sample data: {'1': ['a','b'], '2': ['c','d']}  
# Expected Output: ac ad bc bd  

d1 = {'1': ['a', 'b'], '2': ['c', 'd']}

result = []

for letter1 in d1['1']:
    for letter2 in d1['2']:
        combination = letter1 + letter2
        result.append(combination)
 
print(' '.join(result))






