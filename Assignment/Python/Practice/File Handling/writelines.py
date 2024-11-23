import os
os.chdir("D:\\paras\\Assignment\\Python\\Practice\\File Handling")

# 1. write():
# Write a single line to a file.
# You can write one line at a time using write().

with open("write.txt", "w") as file:
    file.write("This is the first line.\n")  # Writes one line to the file

with open("write.txt", "a") as file:  # Using append mode to add more lines
    file.write("This is the second line.\n")
    file.write("This is the third line.\n")

l1 = ["hello", "paras", "how", "are", "you", "?"]
with open("write.txt", "a") as file:  
    for words in l1:
        file.write(words + "\n")

# 2. writelines():
# Writes a list of lines to a file at once.
# Each item in the list is written as a separate line in the file.

lines_to_write = ["Line 1\n", "Line 2\n", "Line 3\n"]

with open("writelines.txt", "w") as file:
    file.writelines(lines_to_write)  # Writes all lines in the list at once


# Example of appending multiple lines using writelines():
lines_to_append = ["Line 4\n", "Line 5\n"]

with open("writelines.txt", "a") as file:
    file.writelines(lines_to_append)

