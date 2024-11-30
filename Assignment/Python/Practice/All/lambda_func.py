# def double(x):
#     return x*2
# print(double(8))

double = lambda x: x*2
cube = lambda x: x*x*x
avg = lambda *x: sum(x)//len(x)

print(double(8))
print(cube(8))
print(avg(10,20,30))


# Passing function as argument:
def func1(fx, value):
    return 6 + fx(value)

print(func1((lambda x: x*x), 5))
