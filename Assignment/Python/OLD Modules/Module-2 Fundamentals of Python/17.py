# 17. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. 

def swap_n_concat(str1, str2):

    swapped1 = str2[0:2] + str1[2:]
    swapped2 = str1[0:2] + str2[2:]

    st1 = swapped1 + " " + swapped2

    print(st1)
    


str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")

swap_n_concat(str1, str2)




