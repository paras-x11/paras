# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Question 1:
# Write a function that takes a nested list and returns a flattened version of it.

# # Input: [1, [2, [3, 4], 5], 6]
# # Output: [1, 2, 3, 4, 5, 6]

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


l1 = [1,[2,3,4], 5,6, [7,88,9], 0, 33,44,55,[66,777,88]]
l2 = []
for ele in l1:
    if isinstance(ele, list):
        l2.extend(ele)
    else:
        l2.append(ele)
print(l2)