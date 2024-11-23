import os

os.chdir("d:\\paras\\Assignment\\Python\\Practice\\os_module\\Garbage\\folder 1")

path = "Zen of Python.txt"

if os.path.isfile(path):
    print(f"File size: {os.path.getsize(path)} bytes")
else:
    print("File does not exist.")
