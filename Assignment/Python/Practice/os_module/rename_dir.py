import os

os.chdir("d:\\paras\\Assignment\\Python\\Practice\\os_module\\Garbage\\folder 2")

old_dir = "hello"
new_dir = "new_hello"

# First, create the directory to rename (for demonstration purposes)
if not os.path.exists(old_dir):
    os.mkdir(old_dir)
    print(f"Directory '{old_dir}' created.")

# Rename the directory
if os.path.exists(old_dir):
    os.rename(old_dir, new_dir)
    print(f"Directory renamed from '{old_dir}' to '{new_dir}'")
else:
    print(f"Directory '{old_dir}' does not exist.")
