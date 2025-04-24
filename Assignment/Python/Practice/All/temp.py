# l1 = [1,2,5,3,4,5,11,12,13,14,15]
# l2 = [20,30]
# l1.append(l2)


# for i in range(10):
#     print(i)
#     if i==4:
#         break

# else:
#     print("i am else")

# import this


# class person:
#     name = "paras"
#     occupation = "Software developer"
#     networth = 120000

#     def info(self):
#         print(f"{self.name} is {self.occupation}")

# a = person()
# a.name = "Rahul"
# a.occupation = "Accountant"

# b = person ()
# b.name = "Nikita"
# b.occupation = "HR"

# a.info()
# b.info()
# c = person()
# c.info()

# aWESOME is cODING  
# Coding IS Awesome

# st = "aWESOME is cODING"
# print(st)
# st = st.swapcase()
# l1 = st.split()
# print(l1)
# l1.reverse()

# print(" ".join(l1))

# a BLUe MOOn

# st = "a Blue MOON"

# l1 = st.split()

# for word in l1:
#     for i in range(9):
#         if word[0]:
#             print(word[0])
#         else:
#             if ord(ord(word)):
#                  pass
            
# a = 3.12
# b = str(a)
# c = type(b)
# print(type(c))

# name = "Pqrst"
# print(name[-4:-1])
# print(name[1:4])

# l = [1,2,2,3,3,4]
# print(l)
# print(type(l))
# print(l[1])
# l[4] = 4
# print(l, "\n")

# t = (1,2,2,3,3,4)
# print(t)
# print(type(t))
# print(t[1])
# # t[4] = 4
# print(t, "\n")

# s = {1,2,2,3,3,4}
# print(s)
# print(type(s))
# # print(s[1])    # unordered
# # s[4] = 4
# print(s, "\n")

# fs = frozenset({1,2,2,3,3,4})
# print(fs)
# print(type(fs))
# # print(fs[1])
# # fs[4] = 4
# print(fs, "\n")

# print(dir(t))



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


n = 5
for r in range(1, n+1):
    for s in range(n-r):
        print("  ", end="")
    for c in range(2*r-1):
        print("* ", end="")
    print()

for r in range(1, n+1):
    print("  " * (n-r) + "* " * (2*r-1))