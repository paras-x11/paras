# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Question 2:
# Given a dictionary where keys follow the format "group_item", group all values by the group part.


# # Input:
# data = {
#     "fruits_apple": 10,
#     "fruits_banana": 5,
#     "veggies_carrot": 7,
#     "fruits_orange": 8,
#     "veggies_broccoli": 4,
# }

# # Output:
# # {
# #     "fruits": {"apple": 10, "banana": 5, "orange": 8},
# #     "veggies": {"carrot": 7, "broccoli": 4}
# # }
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

data = {
    "fruits_apple": 10,
    "fruits_banana": 5,
    "veggies_carrot": 7,
    "fruits_orange": 8,
    "veggies_broccoli": 4,
}

result = {}

for key, val in data.items():
    
    sep = key.find('_')
    group = key[:sep]
    item = key[sep+1:]
    
    if group not in result:
        result[group] = {}

    result[group][item] = val

print(result)
