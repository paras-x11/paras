
# try:
#     input = int(input("Enter number: "))

# except ValueError:
#     print("input is not an integer.")
    
l = [23,67]
try: 
    p = int(input("Enter position: "))
    print(l[p])

except ValueError:
    print("input is not an integer.")

except IndexError:
    print("Index out of bound error")


