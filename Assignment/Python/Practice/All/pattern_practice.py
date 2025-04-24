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




# 📌 Method 1: Using String Multiplication for Spaces and Stars
# 📌 Method 2: Using Nested Loops for Spaces and Stars



n = 5
for r in range(1, n+1):
    print("* " * r)

# for r in range(1, n+1):
#     for c in range(r):
#         print('* ', end="")
#     print()

# print("\n============================================================\n")

for r in range(n, 0, -1):
    print("* " * r)

# for r in range(n, 0, -1):
#     for c in range(r):
#         print('* ', end="")
#     print()
        
# print("\n============================================================\n")

for r in range(1, n+1):
    print("  " * (n-r) + "* " * r)

# for r in range(1, n+1):
#     for s in range(n-r):
#         print("  ", end="")
#     for c in range(r):
#         print("* ", end="")
#     print()

# print("\n============================================================\n")

for r in range(n, 0, -1):
    print("  " * (n-r) + "* " * r)

# for r in range(n, 0, -1):
#     for s in range(n-r):
#         print("  ",end="")
#     for c in range(r):
#         print("* ", end="")
    # print()

# print("\n============================================================\n")

for r in range(1, n+1):
    print("  " * (n-r) + "* " * (2*r-1))

for r in range(1, n+1):
    for s in range(n-r):
        print("  ", end="")
    for c in range(r*2-1):
        print("* ", end="")
    print()

# print("\n============================================================\n")

for r in range(n, 0, -1):
    print("  " * (n-r) + "* " * (r*2-1))

for r in range(n, 0, -1):
    for s in range(n-r):
        print("  ", end="")
    for c in range(r*2-1):
        print("* ", end="")
    print()

# print("\n============================================================\n")

for r in range(1, n+1):
    for s in range(r-1):
        print("  ", end="")
    for c in range(1):
        print("* ", end="")
    print()

for r in range(n, 0, -1):
    for s in range(r-1):
        print("  ", end="")
    for c in range(1):
        print("* ", end="")
    print()

print("\n============================================================\n")

for r in range(1, n+1):
    for c in range(1, n+1):
        if (r==c) or (r+c) == (n+1):
            print("*", end="")
        else:
            print(" ", end=" ")
    print()

print("\n============================================================\n")

for r in range(1, n+1):
    for c in range(1, n+1):
        if r==1 or r==n or c==1 or c==n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()