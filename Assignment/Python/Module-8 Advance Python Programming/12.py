# 12) Write a Python program to demonstrate the use of local and global variables in a class. 

# Global variable
greeting = "Hello, world!"

class MyClass:
    def __init__(self, name):
        self.name = name  # Instance (local) variable

    def show_variables(self):
        # Local variable
        self.greeting = f"Hello, {self.name}!"
        print(f"Local variable (inside method): {self.greeting}")
        print(f"Global variable (from outside the class): {globals()['greeting']}")             # 'greeting' is key

obj = MyClass("Alice")
obj.show_variables()

print(greeting)
print(obj.greeting)



# Global variables
x = 10
y = 20

def print_globals():
    # Accessing global variables via globals()
    print(globals())

print_globals()

# x is key
print(globals()['x'])