# 3) Write a Python program to create a file and write a string into it.

import os

os.chdir("D:\\paras\\Assignment\\Python\\Module-8 Advance Python Programming")

st = input("Enter string for write it into 3.txt: ")

with open ("3.txt", "w") as f:
    f.write(st)

with open ("3.txt", "r") as f:
    lines = f.read()
    print(lines)