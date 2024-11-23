# create file:
# java is oops lang.
# java is secure lang.

# q1: find oops is exist in this file or not
# q2: find line number which contains lang. word
# q3: replace java with python
 

import os
os.chdir("Python\\Practice\\class work") 
# print(os.getcwd())

with open("task_1.txt", 'w+') as f:                     # for create and write file:
    lines = ['java is oops lang.\n', 'java is secure lang.\n', 'yes now ok\n', 'ok java. how are you\n', 'hello java\n']
    f.writelines(lines)
    f.seek(0)
    print(f.read())



with open("task_1.txt", 'r+') as f:                     # for check oops exist or not and find line which contains 'oops' & 'lang'
    lines = f.readlines()
    # print(lines)
    
    flag = False
    count_oops = []
    count_lang = []
    for index, line in enumerate(lines):
        if 'oops' in line:
            count_oops.append(index+1)
            flag = True

        if 'lang.' in line:
            count_lang.append(index+1)  
    
if flag:
    print("\n-> 'oops' Exist in file")
    print(f"-> 'oops' found at line no: {count_oops}")
else:
    print("\n-> 'oops' Exist in file")

print(f"\n-> 'lang.' found at line no: {count_lang}")        



new_lines = lines                                       
for current_index, new_line in enumerate(new_lines):                # making updated list for update file
    if 'java' in new_line:
        updated_line = new_line.replace('java', 'python')
        new_lines.pop(current_index)
        new_lines.insert(current_index, updated_line)
#     else:
#         print(f"'java' is not in line number {current_index}: {new_line}")
# print("new_lines =", new_lines)



with open ("task_1.txt", 'w+') as f:                            # for see data of file after update
    f.writelines(new_lines) 
    f.seek(0)
    data = f.read()
    print("\n\n\n-> Updated file: ")   
    print(data)  


