import re

# 1. re.match() - Checks if the pattern matches at the beginning of the string.
# Returns a match object if the pattern is found at the start.
result = re.match(r'Hello', 'Hello, World!')
if result:
    print("Match found:", result.group())  # Returns 'Hello'

# 2. re.search() - Searches the entire string for the first occurrence of the pattern.
# Returns a match object if found, or None if not found.
result = re.search(r'fox', 'The quick brown fox jumps over the lazy dog')
if result:
    print("Match found:", result.group())  # Returns 'fox'

# 3. re.findall() - Finds all occurrences of the pattern in the string and returns them as a list.
# Returns a list of all matched substrings found in the string.
result = re.findall(r'\d+', 'There are 123 apples and 456 oranges.')
# This will return a list of all the numbers found: ['123', '456']

# 4. re.finditer() - Returns an iterator of match objects for all occurrences of the pattern.
# This allows you to loop through each match in the string.
for match in re.finditer(r'\d+', 'There are 123 apples and 456 oranges.'):
    print(match.group())  # Each match is returned one by one, like '123' and '456'.

# 5. re.sub() - Replaces the matched pattern with a specified string or function.
# It returns the modified string with the matched text replaced.
text = "The price is $100 and $200."
result = re.sub(r'\$', 'USD', text)  # Replaces '$' with 'USD'
print(result)  # Output: 'The price is USD100 and USD200.'

# 6. re.split() - Splits the string by the occurrences of the pattern.
# It returns a list of substrings resulting from splitting the string by the pattern.
result = re.split(r'\s+', 'This  is   a   test')  # Splits by one or more spaces
# Returns: ['This', 'is', 'a', 'test']

# 7. re.compile() - Compiles a regular expression pattern into a regex object.
# This can improve performance if the pattern is used multiple times.
pattern = re.compile(r'\d+')  # Compiles a pattern to find digits
result = pattern.findall('There are 123 apples and 456 oranges.')
# Finds all occurrences of the pattern in the string
print(result)  # Returns: ['123', '456']

# 8. re.fullmatch() - Checks if the entire string matches the pattern.
# It returns a match object if the whole string matches the pattern, or None if not.
result = re.fullmatch(r'\d{3}-\d{2}-\d{4}', '123-45-6789')  # Matches a social security number format
if result:
    print("Full match found:", result.group())  # Returns '123-45-6789'

# Example of Extracting Emails Using re:
# re.findall() can be used to find all email addresses in a given text.
text = "Please contact us at support@example.com or info@domain.com."
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', text)
# Returns a list of matched email addresses
print("Emails found:", emails)  # Returns: ['support@example.com', 'info@domain.com']
