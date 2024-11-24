# 20) Write a Python program to show method overriding. 

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Create objects of Dog and Cat classes
dog = Dog()
cat = Cat()

dog.speak()   # Overrides Animal's speak() method
cat.speak()   # Overrides Animal's speak() method
