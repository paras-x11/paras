import os
os.chdir("D:\paras\Assignment\Python\Practice\File Handling")
print(os.getcwd())


# Mode	Read	Write	            File Creation	Truncate Existing Content
# 'r+'	Yes	    Yes	                No	            No
# 'w+'	Yes	    Yes	                Yes	            Yes
# 'a+'	Yes	    Yes (append only)	Yes	            No

# # 'r+' Mode: Read and Write (File must exist, no truncation)
# with open("example_r+.txt", "r+") as file:
#     content = file.read()  # Read the existing content
#     print("r+ Mode - Before writing:", content)
#     file.seek(0)  
#     file.write("Updated content")  # Overwrite content

# # 'w+' Mode: Write and Read (File is truncated if it exists)
# with open("example_w+.txt", "w+") as file:
#     file.write("123 Fresh content, Hello world!")  # Write new content
#     print(file.tell())
#     file.seek(0)
#     content = file.read()  # Read the written content
#     print("w+ Mode - After writing:", content)

# 'a+' Mode: Append and Read (Writes at the end, reading possible)
with open("example_a+.txt", "a+") as file:
    file.write("\nAppended content!")  # Append new content
    file.seek(0)  
    content = file.read()  # Read the entire file content
    print("a+ Mode - After appending:", content)
