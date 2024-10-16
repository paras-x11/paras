# 4. Write a Python function to get the largest number, smallest num and sum of all from a list.

def find_min_max_sum(l1):
    min_ele = max_ele = l1[0]
    sum_ele = 0

    for number in l1:
        if number < min_ele:
            min_ele = number
        
        if number > max_ele:
            max_ele = number

        sum_ele += number
    
    print(f"Minimum value: {min_ele}")
    print(f"Maximum value: {max_ele}")
    print(f"Sum of values: {sum_ele}")

elements = input("Enter a list of numbers separated by space: ")
my_list = list(map(int, elements.split()))  
print("List of integers:", my_list)

find_min_max_sum(my_list)


# l1 = [10, 20, 30, 40, 50, 5, 3, 1, 22]
# find_min_max_sum(l1)

# l1 = [10, 20, 30, 40, 50, 5, 3, 1, 22]
# print("Maximum number in list:", max(l1))
# print("Minimum number in list:", min(l1))
# print("sum of all number in list:", sum(l1))






