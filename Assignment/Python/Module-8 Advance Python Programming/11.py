# 11) Write a Python program to create a class and access the properties of the class using an object. 

class Person:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

person1 = Person("Alice", 25)

print(f"Accessing properties directly: Name = {person1.name}, Age = {person1.age}")

print("Accessing properties using a method:")
person1.display_info()
