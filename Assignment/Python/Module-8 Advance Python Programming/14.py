# 14) Write a Python program to show multilevel inheritance. 

class Animal:
    def eat(self):
        print("Animal is eating")

class Mammal(Animal):
    def sleep(self):
        print("Mammal is sleeping")

class Dog(Mammal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.eat()
dog.sleep()
dog.bark()
