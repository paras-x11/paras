# 4) Write a Python program to create a file and print the string into the file.

import os

os.chdir("D:\\paras\\Assignment\\Python\\Module-8 Advance Python Programming")

text = "This is a sample string to be written into the file."

with open("4.txt", "w") as file:
    file.write(text)  

print("String has been written to 4.txt")
