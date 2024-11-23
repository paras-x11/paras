# 15. Practical Example 3: Write a Python program to find a specific string in the list using a simple for loop and if condition.

List1 = ['apple', 'banana', 'mango']

search_string = input("Enter the fruit to search for: ")

found = False
for fruit in List1:
    if fruit == search_string:
        print(f"{search_string} found in the list!")
        found = True
        break

if not found:
    print(f"{search_string} is not in the list.")


# by index:

try:
    index = int(input("Enter an index to access: "))
    print(f"The fruit at index {index} is {List1[index]}")
except IndexError:
    print("Index out of range. Please enter a valid index.")
except ValueError:
    print("Invalid input. Please enter an integer.")
