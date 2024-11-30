# MAP:  map(function, iterable)
numbers = [1, 2, 3, 4, 5]
doubled = map(lambda x: x * 2, numbers)
print(list(doubled))

# FILTER:  filter(predicate, iterable)
numbers = [1, 2, 3, 4, 5]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))

# REDUCE:  reduce(function, iterable)
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x + y, numbers)
print(sum)




# # MAP 
# # def cube(x):
# #   return x * x * x


# # print(cube(2))

# l = [1, 2, 4, 6, 4, 3]
# # newl = []
# # for item in l:
# #   newl.append(cube(item))

# newl = list(map(lambda x: x*x*x, l))
# print(newl)

# # FILTER
# def filter_function(a):
#   return a>2
  
# newnewl = list(filter(filter_function, l))
# print(newnewl)
