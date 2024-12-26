# Define the character to be removed
char_to_remove = '#'

# Open the text file in read mode
with open('Django_Setup_Guide.txt', 'r') as file:
    content = file.read()

# Remove the specific character from the content
content = content.replace(char_to_remove, '')  # Replace 'a' with an empty string

# Open the file in write mode and overwrite with the modified content
with open('Django_Setup_Guide.txt', 'w') as file:
    file.write(content)

print("Character removed successfully.")