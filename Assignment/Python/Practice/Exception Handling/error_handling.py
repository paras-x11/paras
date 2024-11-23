try:
    x = int(input("Enter number: "))
    print(f"Multiplication table of: {x}")

    for i in range(1,11):
        print(f"{x} X {i} = {x*i}")

except Exception as e:
    print(e)
    # print("input is not an integer.")

print("some important line of code")
print("End of Program.")