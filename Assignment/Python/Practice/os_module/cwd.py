import os

# Get current working directory
current_dir = os.getcwd()
print(f"Current Directory: {current_dir}")

# Change to a different directory
new_dir = "d:\\paras\\Assignment\\Python\\Practice\\os_module"
os.chdir(new_dir)
print(f"Changed Directory to: {os.getcwd()}")

os.mkdir("hello_1")