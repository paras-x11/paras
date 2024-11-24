import os
os.chdir("D:\\paras\\Assignment\\Python\\OLD Modules\\Module-4 Advance python programming")

# Open the file in read mode to read all lines
with open("que.txt", "r") as file:
    lines = file.readlines()

# Open the file in write mode to modify it
with open("que.txt", "w") as file:
    for i, line in enumerate(lines, start=1):
        # Replace the first character with the incremented number
        new_line = f"{i}. {line[1:]}" if len(line) > 0 else "\n"
        file.write(new_line)

print("File updated successfully.")
