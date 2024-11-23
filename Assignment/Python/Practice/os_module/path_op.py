import os

os.chdir("d:\\paras\\Assignment\\Python\\Practice\\os_module\\Garbage")

# Join paths

# folder = "my_folder"                                  # for False
# file = "my_file.txt"

folder = "folder 1"                                     # for True
file = "Zen of Python.txt"

# Join the folder and file names to create a complete file path
path = os.path.join(folder, file)  # Combines 'folder' and 'file' into a single path string
print(f"Joined Path: {path}")  # Prints the complete path to the console

# Check if a path exists
print(f"Does the path exist? {os.path.exists(path)}")

# Check if it is a file or directory
print(f"Is it a file? {os.path.isfile(path)}")
print(f"Is it a directory? {os.path.isdir(folder)}")


