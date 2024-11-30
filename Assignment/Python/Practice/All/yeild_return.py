# Function using yield to generate numbers up to n
def count_up_to_with_yield(n):
    for i in range(1, n + 1):
        yield i  # Yield one number at a time

# Function using return to return numbers up to n
def count_up_to_with_return(n):
    numbers = []
    for i in range(1, n + 1):
        numbers.append(i)  # Add each number to the list
    return numbers  # Return the entire list of numbers

# Using yield (generates values one at a time)
print("Using yield:")
gen = count_up_to_with_yield(3)

# Using next() inside a try-except block to handle StopIteration
# Key Points About next():
# - Retrieves the next item: next() pulls the next item from an iterator.
# - Advances the iterator: Moves the iterator to the next value after each call.
# - Exhaustion: Raises StopIteration when there are no more items in the iterator.
# - Optional default value: You can provide a default value, returned when the iterator is exhausted, instead of raising an exception.

while True:
    try:
        print(next(gen))  # Get the next number from the generator
    except StopIteration:
        print("Generator is exhausted.")
        break  # Exit the loop when the generator is exhausted

# Using return (returns all values at once)
# Key Points About return:
# - Ends function execution: return immediately terminates the function and passes a value back to the caller.
# - Returns a value: The function returns the specified value or object (e.g., list, string).
# - Function completion: Once return is called, the function is complete, and no further code is executed.
# - Use case: Best for returning the full result all at once when the entire computation is needed.

print("\nUsing return:")
numbers = count_up_to_with_return(3)
print(numbers)  # Outputs the entire list at once

# Explanation:
# - `yield` pauses the function and generates one value at a time. 
#   It returns a generator object that can be iterated over.
# - `return` ends the function and returns a final value (e.g., list of numbers) all at once.
# - `yield` is memory efficient for large datasets because it generates values lazily (only as needed).
# - `return` gives the entire result immediately but requires storing everything in memory at once.

# Feature            | yield                                                                | return
# -------------------|----------------------------------------------------------------------|-----------------------------------------------
# Behavior           | Pauses function and allows iteration one value at a time.            | Ends function execution and returns a result.
# Returned Object    | Returns a generator object.                                          | Returns the specified value or object (e.g., list, string).
# Memory Efficiency  | Lazy evaluation (only generates values as needed).                   | Stores all values in memory at once.
# State Persistence  | Maintains function state across iterations.                          | Does not maintain state once function ends.
# Use Case           | Best for large data sets or when you need to generate values lazily. | Best for when you need the full result at once.


