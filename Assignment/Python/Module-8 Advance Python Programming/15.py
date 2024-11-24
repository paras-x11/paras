# 15) Write a Python program to show multiple inheritance. 

class Animal:
    def eat(self):
        print("Animal is eating")

class Bird:
    def fly(self):
        print("Bird is flying")

class Bat(Animal, Bird):
    def sleep(self):
        print("Bat is sleeping")

bat = Bat()
bat.eat()    
bat.fly()    
bat.sleep()  

