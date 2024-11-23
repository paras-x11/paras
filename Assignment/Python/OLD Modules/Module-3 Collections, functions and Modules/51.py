# 51. Write a Python function that checks whether a passed string is palindrome or not

s = input("Enter your string: ").lower()


if s == s[::-1]:
    print(f"-> string: '{s}' is palindrome")
else:
    print(f"-> string: '{s}' is not palindrome")
