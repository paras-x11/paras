# 21. Write a Python function to reverses a string if its length is a multiple of 4.

def revstr(str1):
    if len(str1) % 4 == 0:
        return str1[::-1]
    return str1

str1 = input("Enter your string:")

print(revstr(str1))

