print("---1-----------------------------------")


n = 5

for r in range(1, n+1):
    for c in range(r):
        print("* ", end="")
    print("\n", end="")


print("---2-----------------------------------")
for r in range(n, 0, -1):
    for c in range(r):
        print("* ", end="")
        # print(f"{n} ", end="")
    print("\n", end="")


print("---3-----------------------------------")
for r in range(n, 0, -1):
    for s in range(r-1):
        print("  ", end="")
    for c in range((n+1)-r):
        print("* ", end="")
    print("\n", end="")

print("---4-----------------------------------")
for r in range(n):
    for s in range(r):
        print("  ", end="")
    for c in range(n-r):
        print("* ", end="")
    print("\n", end="")

print("---5-----------------------------------")
n = 7
for r in range (1, n+1):
    for s in range(n-r):
        print(" ", end="")
    for c in range(r):
        print("* ", end="")
    print("\n", end="")

print("---6-----------------------------------")
n = 7
for r in range (n):
    for s in range(n-r-1):
        print("  ", end="")
    for c in range(2*r + 1):
        print("* ", end="")
    print("\n", end="")

print("---7-----------------------------------")
n = 7
for r in range (n):
    for s in range(r):
        print("  ", end="")
    for c in range(2*(n-r)-1):
        print("* ", end="")
    print("\n", end="")



 
