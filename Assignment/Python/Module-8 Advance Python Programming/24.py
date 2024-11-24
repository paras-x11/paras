# 24) Python Program to Match a Word in a String Using re.match()

import re

# re.match() only checks if the pattern matches at the beginning of the string.
# It returns a match object if matched, or None if not matched.

text = "The quick brown fox jumps over the lazy dog."
result = re.match(r'The', text)  # Matches 'The' at the start of the string

if result:
    print("Match found:", result.group())  
    print("Match not found.")  