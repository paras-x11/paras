import os
os.chdir("D:\\paras\\Assignment\\Python\\Practice\\File Handling")

with open("truncate.txt", "w") as f:
   f.write("Hello, Paras!")
   f.truncate(5)


with open("truncate.txt", "r") as f:
    print(f.read())