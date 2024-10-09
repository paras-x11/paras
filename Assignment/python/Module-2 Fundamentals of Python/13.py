# 13. Write a Python program to count the number of characters (character frequency) in a string  



str1 = "Hello, World! I am python."

l = 0

for ch in str1:
    if ch.isalpha():
        l += 1

print("Character in your string is: ", l)


