# 5) Write a Python program to read a file and print the data on the console.

import os

os.chdir("D:\\paras\\Assignment\\Python\\Module-8 Advance Python Programming")

file_name = input("Enter file name('3.txt' or '4.txt'): ")

try:
    with open(file_name, "r") as f:
        data = f.read()
    print(data)

except Exception as e:
    print(e)

