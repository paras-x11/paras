# 19. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, 
# if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.

# inputs:
# str1 = "The movie is not that poor."
# str1 = "This movie is amazing."
# str1 = "The movie is not bad."
# str1 = "This film is poor."
# str1 = "The film is poor, not great."
# str1 = "This is a nice movie."                # Error.

str1 = input("Enter your string: ")

index_of_not = str1.find("not")
index_of_poor = str1.find("poor")          # find method returns -1 if substring is not found. (index method gives error)

print("index_of_not =" , index_of_not)
print("index_of_poor =" , index_of_poor)


if index_of_not != -1 and index_of_poor != -1 and index_of_not < index_of_poor:
    result = str1[:index_of_not] + "good" + str1[index_of_poor + 4:]

else:
    result = str1

print(result)

