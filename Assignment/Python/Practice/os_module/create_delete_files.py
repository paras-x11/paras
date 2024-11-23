import os

os.chdir("d:\\paras\\Assignment\\Python\\Practice\\os_module\\Garbage")

# Create a new file
file_name = "my_file.txt"
with open(file_name, 'w') as file:
    file.write("Hello, World!")
    print(f"File '{file_name}' created with some content.")

# Delete the file
if os.path.exists(file_name):
    os.remove(file_name)
    print(f"File '{file_name}' deleted.")
else:
    print(f"File '{file_name}' does not exist.")


