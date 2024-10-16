# 15. Write a Python program to count occurrences of a substring in a string.  

str1 = input("Enter your string: ")

substr = input("Enter substring to count its occurence: ")

print(f'"{substr}" is repeated {str1.count(substr)} times in "{str1}"')


print('"' + substr + '"' + " is reapeted " + str(str1.count(substr)) + " times in " + '"' + str1 + '"')