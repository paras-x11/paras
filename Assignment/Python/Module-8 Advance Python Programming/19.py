# 19) Write a Python program to show method overloading.

class Calculator:
    def add(self, *args):
        result = 0
        for num in args:
            result += num
        return result

calc = Calculator()
print(calc.add(2, 3))        
print(calc.add(1, 2, 3, 4))  
print(calc.add(1, 2, 3, 4, 5, 6))




class Printer:
    def print_message(self, message="Hello"):
        print(message)

printer = Printer()

printer.print_message()
printer.print_message("Hello, World!")

