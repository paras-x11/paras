# 12. Write a Python program to calculate the length of a string.  

str1 = "Hello, World! I am python."

l = 0

for ch in str1:
    l += 1

print("Length of your string is: ", l)


#----------------------------------------------------#

str2 = input("\nEnter string: ")

print("Length of your string is: ", len(str2))

