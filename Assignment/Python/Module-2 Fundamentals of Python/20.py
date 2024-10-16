# 20. Write a Python function that takes a list of words and returns the length of the longest one

str1 = input("Enter your string: ").split()

my_list = list(str1)

max_len = len(str1[0])

for index, words in enumerate(my_list):
    if len(words) > max_len:
        max_len = len(words)
        max_word = words

print(f"\nLongest word is: {max_word} and \nits length is: {max_len}")



# for words in my_list:
#     if len(words) > max_len:
#         max_len = len(words)
# print("longest length is:", max_len)
    




