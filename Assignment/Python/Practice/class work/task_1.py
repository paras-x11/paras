# create file:

# java is oops lang.
# java is secure lang.

# q1: fine oops is exis in this file or not
# q2: file line number which contains lang. word
# q3: replace java with python

import os
os.chdir("D:\paras\Assignment\Python\Practice\class work")
# print(os.getcwd())

# Creating and writing to the file
with open("task_1.txt", 'w+') as f:
    lines = ['java is oops lang.\n', 'java is secure lang.\n', 'yes now ok\n', 'ok java. how are you\n', 'hello java\n']
    f.writelines(lines)
    f.seek(0)
    print(f.read())  # Print file contents after writing


# Reading and processing the file
with open("task_1.txt", 'r+') as f:
    lines = f.readlines()

    # Q1: Check if 'oops' exists in the file
    flag = False
    count_oops = []
    count_lang = []

    for index, line in enumerate(lines):
        if 'oops' in line:
            count_oops.append(index + 1)  
            flag = True

        if 'lang.' in line:
            count_lang.append(index + 1)  

    # Q1 Output
    if flag:
        print("\n-> 'oops' exists in the file")
        print(f"-> 'oops' found at line no: {count_oops}")
    else:
        print("\n-> 'oops' does not exist in the file")

    # Q2 Output
    print(f"\n-> 'lang.' found at line no: {count_lang}")

# Q3: Replace 'java' with 'python'
new_lines = []

for line in lines:
    updated_line = line.replace('java', 'python')
    new_lines.append(updated_line)

# Write updated lines back to the file
with open("task_1.txt", 'w+') as f:
    f.writelines(new_lines)
    f.seek(0)
    data = f.read()

    print("\n\n\n-> Updated file:")
    print(data)  