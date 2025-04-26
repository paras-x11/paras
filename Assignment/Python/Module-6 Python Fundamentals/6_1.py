# 17. Write a generator function that generates the first 10 even numbers.

def generate_even_numbers(num):
    for i in  range(1, num+1):
        yield i * 2

gen = generate_even_numbers(10)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# for num in generate_even_numbers(10):
#     print(f"{num},", end="")


