# 21. Write a Python program to convert a tuple to a string.

tup = (12,15,17,22,"hello")

s = ""
for ele in tup:
    s = s + str(ele) + " "
print(s)


tup = (12, 15, 17, 22, "hello")
s = " ".join(map(str, tup))

print(s) 

