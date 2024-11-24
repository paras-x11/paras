# 18) Write a Python program to demonstrate the use of super() in inheritance.

class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal {self.name} created")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        print(f"Dog {self.name} of breed {self.breed} created")

dog = Dog("Buddy", "Golden Retriever")
