
# normal iterative approach
def fibonacci(n):
    a = 0
    b = 1

    li = []
    li.append(a)
    li.append(b)
    for _ in range(2, n):
        f = a + b

        a = b
        b = f

        li.append(f)
    print(li)

fibonacci(8)



# Recursive Fibonacci function

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Get number of terms from the user
terms = int(input("Enter the number of terms: "))
fib_sequence = [fibonacci(i) for i in range(terms)]
print("Fibonacci sequence:", fib_sequence)





