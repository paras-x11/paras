# 1. Write a Python program to demonstrate string slicing.
message = "Hello, World!"
# Slicing the string from index 0 to 5
substring = message[:5]
print(substring)  # Output: Hello

# Slicing the string from index 7 to end
substring2 = message[7:]
print(substring2)  # Output: World!

# Slicing the string from index 2 to 9
substring3 = message[2:9]
print(substring3)  # Output: llo, Wo

# 2. Write a Python program that manipulates and prints strings using various string methods.
text = "  Python is fun!  "
# Strip whitespace from both ends
stripped_text = text.strip()
print(stripped_text)  # Output: Python is fun!

# Convert to uppercase
uppercase_text = text.upper()
print(uppercase_text)  # Output:   PYTHON IS FUN!  

# Convert to lowercase
lowercase_text = text.lower()
print(lowercase_text)  # Output:   python is fun!  

# Replace 'fun' with 'awesome'
replaced_text = text.replace("fun", "awesome")
print(replaced_text)  # Output:   Python is awesome!  

# Find the position of 'is' in the string
position = text.find("is")
print(position)  # Output: 9
