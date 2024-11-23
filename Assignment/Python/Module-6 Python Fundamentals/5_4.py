# 16. Practical Example 4: Print this pattern using nested for loop:
# *
# **
# ***
# ****
# *****

n = 5

# for r in range(1, n+1):
#     for c in range(r):
#         print("* ", end="")
#     print("\n", end="")

# for r in range(n, 0, -1):
#     for c in range(r):
#         print("* ", end="")
#     print("\n", end="")


# for r in range(n, 0, -1):
#     for s in range(r-1):
#         print("  ", end="")
#     for c in range((n+1)-r):
#         print("* ", end="")
#     print("\n", end="")

# for r in range(n):
#     for s in range(r):
#         print("  ", end="")
#     for c in range(n-r):
#         print("* ", end="")
#     print("\n", end="")

# n = 7
# for r in range (1, n+1):
#     for s in range(n-r):
#         print(" ", end="")
#     for c in range(r):
#         print("* ", end="")
#     print("\n", end="")

# n = 7
# for r in range (n):
#     for s in range(n-r-1):
#         print("  ", end="")
#     for c in range(2*r + 1):
#         print("* ", end="")
#     print("\n", end="")

n = 7
for r in range (n):
    for s in range(r):
        print("  ", end="")
    for c in range(2*(n-r)-1):
        print("* ", end="")
    print("\n", end="")


 