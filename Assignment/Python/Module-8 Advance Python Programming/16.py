# 16) Write a Python program to show hierarchical inheritance. 

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

dog = Dog()
cat = Cat()

dog.speak()
dog.bark()

cat.speak()
cat.meow()
