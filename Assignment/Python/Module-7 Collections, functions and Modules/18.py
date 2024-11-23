# 18) Write a Python program to count how many times each character appears in a string.

my_string = "hello world"

char_count = {}
for char in my_string:
    char_count[char] = char_count.get(char, 0) + 1

print("Character counts:", char_count)



from collections import Counter
st = "Hello, world! I am Python aka py."

char_counter = Counter(st)

print("Character counts:", dict(char_counter))



my_string = "hello world, How are you?"

char_count = {}
for char in set(my_string):  # Using set to avoid redundant counting
    char_count[char] = my_string.count(char)

print("Character counts:", char_count)

