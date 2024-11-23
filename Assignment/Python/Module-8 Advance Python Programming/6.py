# 6) Write a Python program to check the current position of the file cursor using tell().

import os

os.chdir("D:\\paras\\Assignment\\Python\\Module-8 Advance Python Programming")

file_name = input("Enter file name('3.txt' or '4.txt'): ")

try:
    with open(file_name, "r") as f:
        start_pos = f.tell()
        data = f.read()
        
        end_pos = f.tell()
    print(start_pos)
    print(data)
    print(end_pos)

except Exception as e:
    print(e)