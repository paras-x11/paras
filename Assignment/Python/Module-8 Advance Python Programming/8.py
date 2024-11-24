#  8) Write a Python program to handle multiple exceptions (e.g., file not found, division by zero). 



try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    print(f"{a} / {b} = {a/b}")

except ValueError as ve:
    print("\n-> Enter valid integer.", ve)

except ZeroDivisionError as de:
    print("\n-> Can not divide by zero.", de)

except Exception as e:
    print("\n-> An unexpected error occured.", e)


try:
    with open("temp.txt", 'r') as f:
        data = f.read()
        print(data)
except FileNotFoundError as e:
    print(e)


