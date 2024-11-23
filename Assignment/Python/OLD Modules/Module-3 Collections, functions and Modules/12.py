# 12. Write a Python program to convert a list of characters into a string.

def listToString(l1):
    return "".join(l1)


l1 = ['H','e','l','l','o',' ','P','a','r','a','s']

s = ""

for ch in l1:
    s = s + ch
print(s)

s = listToString(l1)
print(s)



