# 16. Write a Python program to count the occurrences of each word in a given sentence 


sentence = input("Enter a sentence: ").lower()

my_list = sentence.split()

word_count = {}

for word in my_list:
    if word in word_count:
        word_count[word] += 1  # Increment count if the word is already in the dictionary means giving values to key: key is words and value is numbers
    else:
        word_count[word] = 1   # Initialize count to 1 if the word is not in the dictionary

print("Word occurrences:")
for word, count in word_count.items():
    print(f"{word}: {count}")



# this is for individual character..
# str1 = "Hello there, i am Python.".lower()

# empty_str = ""

# for ch in str1:
#     if ch not in empty_str:
#         empty_str += ch
#         occurence = str1.count(ch)
#         print(f'{ch} - occurs: {occurence}')
# print(empty_str)


