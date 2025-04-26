# ### 📌 Comprehensions & Lambda


# 51. List of squares using list comprehension.
l1 = [x for x in range(1, 26)]
print(l1)

l2 = [x**2 for x in l1]
print(l2)

# 52. Dictionary from two lists using dict comprehension.
d1 = {k: v for k, v in zip(l1, l2)}
print(d1)

# 53. Filter even numbers using `filter()` and lambda.
l3 = list(filter(lambda x: x%2==0, l2))
print(l3)

# 54. Sort a list of tuples by second item using lambda.
students = [("Alice", 90), ("Bob", 85), ("Charlie", 95), ("Naruto", 74)]
print(students[1][1])
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)



# 55. Map lowercase to uppercase using `map()`.
l4 = []

for tup in sorted_students:
    tup_data = (tup[0].lower(), tup[1])
    l4.append(tup_data)
print(l4)


l5 = list(map(lambda x: x[0].lower(), sorted_students))
print(sorted_students)
print(l5)

def make_lowercase(data):
    l6 = []
    for i in data:
        if isinstance(i, str):
            l6.append(i.lower())
        else:
            l6.append(i)
    return l6

l7 = ['Alice', 'bOB', 'CharLie', 'daVid', 'EVE']
print(make_lowercase(l7))