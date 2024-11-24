# 23) Python Program to Search for a Word in a String Using re.search()

import re

# re.search() searches the entire string for the first occurrence of the pattern.
# It returns a match object if found, or None if not found.

text = "The quick brown fox jumps over the lazy dog."
result = re.search(r'fox', text)  # Searches for the word 'fox'

if result:
    print("Match found:", result.group())  
else:
    print("Match not found.")  