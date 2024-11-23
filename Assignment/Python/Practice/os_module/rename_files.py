import os

os.chdir("d:\\paras\\Assignment\\Python\\Practice\\os_module\\Garbage\\folder 2")

# Renaming a file
original_file = "temp.txt"
new_file = "new_name.txt"

# Create a file to rename
if not os.path.exists(original_file):
    with open(original_file, 'w') as file:
        file.write("Sample content.")

if os.path.exists(original_file):
    os.rename(original_file, new_file)
    print(f"File renamed from '{original_file}' to '{new_file}'.")
else:
    print(f"File '{original_file}' does not exist.")


# ----------------------------------------------------------------------------------------- #
