# 58. Write a Python program to read a random line from a file


# To read a random line from a file, you can use the random.choice() function 
# along with reading the file's contents into a list.

import random

# Step 1: Specify the file path
file_path = r'D:/paras/Assignment/Python/Module-3 Collections, functions and Modules/58text.txt'

# Step 2: Open the file and read its contents
with open(file_path, 'r') as file:
    lines = file.readlines()                                            # Read all lines into a list

# Step 3: Choose a random line from the list
if lines:                                                               # Check if the list is not empty
    random_line = random.choice(lines)
    
    # Step 4: Display the random line
    print(random_line.strip())                                          # Use strip() to remove any leading/trailing whitespace
else:
    print("The file is empty.")

