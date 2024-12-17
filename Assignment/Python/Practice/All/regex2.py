import re

str = "Roy is 43 Babu is 27 RoHaN is 35 SohaM is 18 balA is 29"

# print(re.match(r'[A-Z][a-z]*', str))   # Checks if the pattern matches at the beginning of the string.
# print(re.search(r'[A-Z][a-z]*', str))   # Returns a match object if found(only 1st occurence), or None if not found.

# match_result = re.findall(r'[A-Z]', str)
# search_result = re.findall(r'[A-Z][a-z]*', str)   

# print(match_result)
# print(search_result)

print(re.match("^[a-z0-9]+@tops-int.com$","test@tops-int.com6"))