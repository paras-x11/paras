# 23. Write a Python function to insert a string in the middle of a string.


def addString_Middle(original_str, add):
    middle_position = len(original_str) // 2
    new_str = original_str[:middle_position] + add + original_str[middle_position:]
    return new_str

def addString(original_str, add, position):
    if position < 0:
        position = 0
    elif position > len(original_str):
        position = len(original_str)

    new_str = original_str[:position] + add + original_str[position:]
    return new_str

sentence = "Hello there, how are you"
print("Original sentence:", sentence)
print("Length is:", len(sentence))

print("\nChoose an option:")
print("1. Add at a specific position")
print("2. Add in the middle")

choice = input("Enter your choice (1 or 2): ")

match choice:
    case '1':
        position = int(input("\nEnter position where you want to insert: "))
        add = input("Enter what you want to add: ")
        result = addString(sentence, add, position)
    case '2':
        add = input("Enter what you want to add in the middle: ")
        result = addString_Middle(sentence, add)
    case _:
        result = "Invalid choice! Please enter 1 or 2."

print("\nResulting sentence:", result)
