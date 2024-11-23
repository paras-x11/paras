import os
os.chdir("D:\\paras\\Assignment\\Python\\Practice\\File Handling")

# 1. readline():
# Reads only one line from the file at a time.
# Each call to readline() reads the next line in the file until the end is reached.
# It’s useful when you want to process a file line-by-line without loading the entire file into memory.

with open("readlines.txt", "r") as file:
    line = file.readline()
    print(line)  # Prints the first line of the file

with open("readlines.txt", "r") as file:
    line1 = file.readline()  # Reads the first line
    line2 = file.readline()  # Reads the second line
    line3 = file.readline()  # Reads the third line
    # And so on...
print(line1)
print(line2)
print(line3)


# ACCESSING SPECIFIC LINE:
with open("readlines.txt", "r") as file:
    for _ in range(4):  # Skip the first 4 lines
        file.readline()
    fifth_line = file.readline()  # Read the 5th line
    print(fifth_line)

# Each time through the loop, file.readline() reads and discards one line. So, after 4 iterations, the first 4 lines have been read and skipped.


# 2. readlines():
# Reads all lines from the file at once and returns them as a list of strings, where each item in the list is a line from the file.
# Useful when you want to work with all lines at once, but can use more memory for large files.

with open("readlines.txt", "r") as file:
    lines = file.readlines()
    print(lines)  # Prints a list of all lines in the file


f = open('readlines.txt', 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()








