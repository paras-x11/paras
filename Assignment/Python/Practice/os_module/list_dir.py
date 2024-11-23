import os


# List all files and folders in the current directory
items = os.listdir()
print("Contents of the Directory:", items)

# List all files and folders in a specific directory
specific_dir = "d:\\paras\\Assignment\\Python\\Practice"
items_in_specific_dir = os.listdir(specific_dir)
print(f"Contents of {specific_dir}:", items_in_specific_dir)
