import os

os.chdir("d:\\paras\\Assignment\\Python\\Practice\\os_module\\Garbage")

# Create a new directory
dir_name = "folder 1"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    print(f"Directory '{dir_name}' created.")
else:
    print(f"Directory '{dir_name}' already exists.")

# Remove a directory (must be empty)
if os.path.exists(dir_name):
    os.rmdir(dir_name)
    print(f"Directory '{dir_name}' removed.")
else:
    print(f"Directory '{dir_name}' does not exist.")
