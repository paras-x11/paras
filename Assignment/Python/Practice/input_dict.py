d = {}

while True:
    key = input("Enter key(enter 'stop' for exit): ")
    if key == 'stop':
        break
    val = input("Enter value: ")

    d[key] = val

print(d)


d1 = {}
len_of_dict = int(input("Enter how many key-value pairs you want to add: "))

for i in range(len_of_dict):
    key = input("Enter key: ")
    val = input("Enter value: ")

    d1[key] = val

print(d1)
