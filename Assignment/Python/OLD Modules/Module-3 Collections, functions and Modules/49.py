# 50. Write a Python function to check whether a number is in a given range

# starting_point = int(input("enter starting point of range: "))
# ending_point = int(input("enter ending point of range: "))

# r = [num for num in range(starting_point, ending_point+1)]


r = [num for num in range(10, 21)]


check = int(input("enter value for check in range: "))

if check in r:
    print(f"{check} is member of given range.")
else:
    print(f"{check} is not a member of given range")



print("your range is:", r)


