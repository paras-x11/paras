# 2.  Write a Python program to read an entire text file.  

import os
os.chdir("D:\\paras\\Assignment\\Python\\OLD Modules\\Module-4 Advance python programming")

with open("demo.txt", "a") as f:
    f.write("hello, World!\n")

with open("demo.txt") as f:
    data = f.read()
    print(data)

