# 6. Write a Python program to count the number of strings where the string length is 2 or more and 
# the first and last character are same from a given list of strings. 

string_list = [ "abc", "aba", "xyx", "hello", "wow", "noon", 
                "ab", "cd", "deed", "pop", "level", "aa",
                "racecar", "madam" ]

count = 0

for string in string_list:
    if len(string) >= 2:
        if string[0] == string[-1]:
            # print(string)
            count+=1

print(count)








