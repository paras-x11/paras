# 46. Write a Python program to combine values in python list of dictionaries.
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':300},  {'item': 'item1', 'amount': 750}]
# Expected Output: Counter ({'item1': 1150, 'item2': 300})

l1 = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':300}, {'item': 'item1', 'amount': 750}, {'item': 'item3', 'amount': 900}, ]

result = {}

for ele in l1:
    item = ele['item']
    val = ele['amount']

    if item in result:
        result[item] += val
    else:
       result[item] = val

print(result)

result['hello'] = "world"

print(result)

result['hello'] = 50

print(result)




