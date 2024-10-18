# 14. Write a Python program to find the second smallest number in a list. 


def find2ndSmallest(l):

    l1 = list(map(int, l))          # Convert to integers
    l1 = list(set(l1))              # Remove duplicates
    l1.sort()                       # Sort the list
    
    if len(l1) < 2:
        print("Not enough unique numbers to find the second smallest.")
    else:
        print(f"Second smallest number is: {l1[1]}")


my_list = list(input("Enter elements separated by space: ").split())  

find2ndSmallest(my_list) 
