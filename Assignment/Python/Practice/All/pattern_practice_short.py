print("---String Multiplication-----------------")
print("---1-------------------------------------")

n = 5
for i in range(1, n+1):
    print("* " * i)


print("---2-------------------------------------")

n = 5
for i in range(n, 0, -1):
    print("* " * i)

print("---3-------------------------------------")
n = 5
for i in range(n, 0, -1):
    print("  " * (n-i) + "* " * i)

print("---4-positive loop------------------------------------")
n = 5
for i in range(1, n+1):
    print("  " * (n-i) + "* " * (i))

print("---4-negative loop------------------------------------")
n = 5
for i in range(n, 0, -1):
    print("  " * (i-1) + "* " * (n-i+1))