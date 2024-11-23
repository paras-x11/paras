# 17. Write a generator function that generates the first 10 even numbers.

def generate_even_numbers():
    for i in  range(1, 11):
        yield i * 2

for num in generate_even_numbers():
    print(f"{num},", end="")


