# ### 📌 Strings:


# 6. Count vowels in a string.
# text = input("enter text: ").lower()

# vowels = ['a', 'e', 'i', 'o', 'u']
# count = 0
# for char in text:
#     if char in vowels:
#         count += 1
# print(f"there are {count} vowels in: {text}")

# 7. Check if a string is a palindrome.
# text = input("enter string: ")
# rev = text[::-1]
# if text == rev:
#     print(f"{text} is palindrome")
# else:
#     print(f"{text} is not a palindrome")


# 8. Remove duplicates from a string.
# text = input("enter string: ")

# unique_set = set(text)

# result = ''.join(unique_set)
# print(result)



# 9. Find frequency of each character.
text = input("enter string: ")

char_frequencies = {}
count = 0

for char in text:
    if char in char_frequencies:
        char_frequencies[char] += 1
    if char not in char_frequencies:
        char_frequencies[char] = 1
print(char_frequencies)
            



# 10. Reverse each word in a sentence.
sentence = input("enter sentence: ")

words = sentence.split()

print(words)

for index, word in enumerate(words):
    words[index] = word[::-1]

print(words)