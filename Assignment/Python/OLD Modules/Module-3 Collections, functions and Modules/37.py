# 37. Write a Python script to print a dictionary where the keys are numbers between 1 and 15.  

my_dict = {
    i: chr(i+96) for i in range(1,16)
}

print(my_dict)


my_dict2 = {
    i: i**2 for i in range(1,16)
}

print(my_dict2)