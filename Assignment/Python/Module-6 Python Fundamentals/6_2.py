# 18. Write a Python program that uses a custom iterator to iterate over a list of integers. 


class IntegerListIterator:
    def __init__(self, integer_list):
        self.integer_list = integer_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.integer_list):
            current_value = self.integer_list[self.index]
            self.index += 1
            return current_value
        else:
            raise StopIteration

integers = [1, 2, 3, 4, 5]
iterator = IntegerListIterator(integers)

for number in iterator:
    print(number)


# __init__: Initializes the iterator with a list of integers and sets the starting index to 0.
# __iter__: Returns the iterator object itself, allowing it to be used in a for loop.
# __next__: Retrieves the next item from the list. If the index is beyond the list length, it raises a StopIteration exception, ending the iteration.