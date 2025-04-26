# ## 🧠 **Intermediate Level – Logic & Structures**

# ### 📌 Dictionaries & Sets

# 16. Count word occurrences in a paragraph.
paragraph = "The sun dipped below the horizon, casting a warm golden glow across the landscape.\nBirds fluttered through the trees, their songs filling the air with a melody that seemed to dance with the breeze.\nIn the distance, the soft murmur of a stream blended with the rustling of leaves, creating a peaceful harmony that calmed the mind.\nAs the evening sky deepened into shades of purple and orange, the world seemed to slow, as though it too was taking a moment to breathe.\nA sense of tranquility settled over the land, and for a brief moment, time itself seemed to stand still."
# print(paragraph)
# word_list = paragraph.split()

# word_count = {}

# for word in word_list:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1

# for key, val in word_count.items():
#     print(f"{key}: {val}") 
     

# 17. Sort a dictionary by value.
people_ages = {"Alice": 28, "Bob": 34, "Charlie": 22, "Diana": 30, "Eve": 25, "Frank": 40, "Grace": 27, "Hank": 33, "Ivy": 29, "Jack": 24, "Karen": 38, "Leo": 21, "Mona": 32, "Nate": 26, "Olivia": 35, "Paul": 31, "Quinn": 23, "Rachel": 36, "Steve": 28, "Tina": 20}

# Sort the dictionary by values in ascending order
sorted_people_ages = dict(sorted(people_ages.items(), key=lambda item: item[1]))

print(sorted_people_ages)




# 18. Find duplicate values in dictionary keys.
people_ages = { "Alice": 28, "Bob": 34, "Charlie": 22, "Diana": 30, "Eve": 25, "Frank": 40, "Grace": 28, "Hank": 33, "Natasha": 22}

value_count = {}

for val in people_ages.values():
    if val in value_count:
        value_count[val] += 1
    else:
        value_count[val] = 1

duplicate_vals = []

for key, val in value_count.items():
    if val > 1:
        duplicate_vals.append(key)
print("duplicate Values: ", duplicate_vals)
 


# 19. Merge two dictionaries.
dict1 = {"Alice": 28, "Bob": 34}
dict2 = {"Charlie": 22, "Diana": 30}

dict1.update(dict2)
print("Merged Dictionary:", dict1)


# 20. Invert a dictionary (value becomes key).
data = {"Alice": 28, "Bob": 34, "Charlie": 22, "Diana": 30, "Eve": 25, "Frank": 40, "Grace": 27, "Hank": 33}

keys_to_remove = list(people_ages.keys())  

for key in keys_to_remove:
    value = people_ages[key]
    people_ages[value] = key  # Swap key and value
    del people_ages[key]  # Delete the original key-value pair

print("Inverted Dictionary:", people_ages)
