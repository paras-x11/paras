# 34. Write a Python script to check if a given key already exists in a dictionary. 

my_dict = {1: 'H', 2: 'e', 3: 'l', 4: 'l', 5: 'o', 6: ' ', 7: 'W', 8: 'o', 9: 'r', 10: 'l', 11: 'd', 12: '!'}

key_to_check = int(input("Enter key to check(1 to 15): "))

if key_to_check in my_dict:
    print("Exist")
else:
    print("not exist.")



# 34. Write a Python script to check if a given key already exists in a dictionary. 


my_dict = {1: 'H', 2: 'e', 3: 'l', 4: 'l', 5: 'o', 6: ' ', 7: 'W', 8: 'o', 9: 'r', 10: 'l', 11: 'd', 12: '!'}

key_to_check = input("Enter key to check(1 to 15): ")

flag = False

for key in my_dict.keys():
    if key_to_check == key:
        flag = True

if flag:
    print("Exist")
else:
    print("not exist.")
        
        