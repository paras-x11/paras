# Here's a structured **Python Core to Advanced** practice problem list, covering **all key concepts**, from beginner to expert level. You can go through them step-by-step or pick areas you want to focus on.

# ---

# ## 🐍 **Beginner Level – Core Python Practice**

# ### 📌 Basic Syntax & Variables
# 1. Write a program to swap two variables.
# 2. Check if a number is even or odd.
# 3. Find the largest among 3 numbers.
# 4. Take user input and reverse it.
# str1 = input("enter input: ")
# print(str1[::-1])
# 5. Calculate area and perimeter of a rectangle/circle.

# ### 📌 Strings
# 6. Count vowels in a string.
# 7. Check if a string is a palindrome.
# 8. Remove duplicates from a string.
# 9. Find frequency of each character.
# 10. Reverse each word in a sentence.

# ### 📌 Lists & Tuples
# 11. Find the second largest element in a list.
# import random as r
# l1 = [x for x in range(1, 101) if x%2==0]
# print(l1)
# l2 = [r.choice(range(1, 101)) for _ in range(15)]
# print(l2)
# l2.sort()
# print(l2)
# print(l2[-2])
# 12. Remove duplicates from a list.
# 13. Merge two sorted lists into one.
# 14. Flatten a nested list.
# l3 = [1,[2,3,4], 5,6, [7,88,9], 0, 33,44,55,[66,777,88]]
# l4 = []
# for ele in l3:
#     if isinstance(ele, list):
#         l4.extend(ele)
#     else:
#         l4.append(ele)
# print(l4)

# 15. Find the common elements in two lists.
# l5 = [58, 56, 6, 75, 20, 93, 1, 66, 60, 81, 2, 43, 25, 89, 99]
# l6 = [6, 53, 81, 23, 100, 24, 89, 58, 12, 69, 15, 75, 52, 13, 66]
# l7 = []

# for ele1 in l5:
#     for ele2 in l6:
#         if ele1 == ele2:
#             l7.append(ele1)
#             continue
# print(l7)
# ---

# ## 🧠 **Intermediate Level – Logic & Structures**

# ### 📌 Dictionaries & Sets
# 16. Count word occurrences in a paragraph.
# madara = """Madara Uchiha (Japanese: うちは マダラ, Hepburn: Uchiha Madara) is a fictional character and one of the main antagonists in Masashi Kishimoto's manga (and anime adaptation) Naruto. He appears for the first time in "Part II" of the manga and the Shippuden anime adaptation (During the Fourth Shinobi War arc).

# He, along with its first Hokage Hashirama Senju, is one of the co-founders of Konohagakure (Japanese: 木ノ葉隠れの里, Hepburn: Konohagakure no Sato) village from the ninja world. Their power conflict over how to run the village, as well as the long-time feud between clans, leads to Madara deciding that humanity is beyond saving and seeks to cast a genjutsu (infinite tsukuyomi) on the entire planet, however, he isn't aware that this plan will eventually annihilate humanity and turn them into numerous variants of White Zetsu. This leads to his defection and death in a battle with Hashirama; however, it is revealed later that Madara secretly revived himself, surviving well into elderhood, and manipulating Obito Uchiha into laying the key for his future plans before his true death.""".lower()

# word = input('enter any word to count: ').lower()
# count = madara.count(word)
# print(count)
# 17. Sort a dictionary by value.
# 18. Find duplicate values in dictionary keys.
# 19. Merge two dictionaries.
# 20. Invert a dictionary (value becomes key).

# ### 📌 Loops & Conditionals
# 21. Print a pattern using nested loops.
# 22. FizzBuzz problem.
# 23. Check for prime numbers.
# 24. Print all Armstrong numbers in a range.
# 25. Create a simple calculator.

# ### 📌 Functions & Recursion
# 26. Write a recursive function to find factorial.
# 27. Recursive Fibonacci sequence.
# 28. Check if a string is a palindrome using recursion.
# 29. Implement a decorator to log function execution.
# 30. Use `*args` and `**kwargs` in a sample function.

# ---

# ## 🧩 **Advanced Level – OOP, File Handling, Exception, Modules**

# ### 📌 Object-Oriented Programming
# 31. Create a class for `BankAccount` with deposit and withdraw.
class BankAccount:
    def __init__(self, acc_holder):
        self._acc_holder = acc_holder
        self.balance = 0
    def deposit(self, amt):
        if amt > 0:
            self.balance += amt
            print(f'₹{amt} deposited successfully. Total Balance is: ₹{self.balance}')
        else:
            print(f'Enter positive amount. Total Balance is: ₹{self.balance}')


# 32. Implement inheritance: `Vehicle -> Car, Bike`.
# 33. Use @property decorators for a class.
# 34. Overload operators using magic methods (`__add__`, `__str__`).
# 35. Design a simple library management system with classes.

# ### 📌 File Handling
# 36. Read from a file and count word frequency.
# 37. Append new lines to an existing file.
# 38. Merge two text files into one.
# 39. Read a CSV file and display content.
# 40. Remove blank lines from a file.

# ### 📌 Exception Handling
# 41. Handle division by zero.
# 42. Custom exception class for age validation.
# 43. Try-Except-Else-Finally structure example.
# 44. Nested exception handling demo.
# 45. Raise a custom error if password is weak.

# ### 📌 Modules & Packages
# 46. Create and import your own module.
# 47. Use built-in modules: `datetime`, `random`, `os`, `math`.
# 48. List all files in a directory.
# 49. Zip and unzip folders using `zipfile`.
# 50. Use `argparse` for command-line input.

# ---

# ## 🚀 **Expert Level – Advanced Python Practice**

# ### 📌 Comprehensions & Lambda
# 51. List of squares using list comprehension.
# 52. Dictionary from two lists using dict comprehension.
# 53. Filter even numbers using `filter()` and lambda.
# 54. Sort a list of tuples by second item using lambda.
# 55. Map lowercase to uppercase using `map()`.

# ### 📌 Generators & Iterators
# 56. Create a generator to yield prime numbers.
# 57. Custom iterator class for Fibonacci numbers.
# 58. Generator expression vs list comprehension example.
# 59. Use `yield from` for nested generators.
# 60. Memory usage comparison: list vs generator.

# ### 📌 Functional Programming
# 61. Use `reduce()` to multiply all elements in a list.
# 62. Create a function that returns another function.
# 63. Closure that remembers a counter.
# 64. Memoization using `functools.lru_cache`.
# 65. Function chaining example.

# ### 📌 Multithreading & Multiprocessing
# 66. Create a thread to print numbers.
# 67. Use `ThreadPoolExecutor` to run multiple tasks.
# 68. Compare time: single-threaded vs multi-threaded.
# 69. Use `multiprocessing` to calculate squares of numbers.
# 70. Shared memory example in multiprocessing.

# ### 📌 Decorators & Context Managers
# 71. Create a timer decorator.
# 72. Write a custom context manager using `with`.
# 73. Use `contextlib` to simplify context manager.
# 74. Decorator to repeat function 3 times.
# 75. Decorator that logs function args and return values.

# ---

# Would you like me to make this into a PDF or a structured Notion/Markdown document you can follow step by step?