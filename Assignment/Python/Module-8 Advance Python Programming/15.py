# 15) Write a Python program to show multiple inheritance. 

class Animal:
    def eat(self):
        print("Animal is eating")

class Bird:
    def fly(self):
        print("Bird is flying")

    def sleep(self):
        print("Bird is sleeping")

class Bat(Animal, Bird):
    def fly(self):
        print("bat flying")

    def sleep(self):
        print("Bat is sleeping")

bat = Bat()
bat.eat()    
bat.fly()    
bat.sleep()  



# 🔹 Method Resolution Order (MRO) for Bat:
# The MRO determines the order in which Python looks for methods:
# Bat then-> Animal then->  Bird  -- bcoz class Bat(Animal, Bird)

# In this case:
# Python will first check the Bat class for the method.
# If it's not found there, it will check Animal.
# Then it will check Bird (but only for methods not defined in Bat).

# Finally, if no method is found, it would fall back to object means It Will raise AttributeError, because it is not found in any class, and it will fall back to object,
# Normally, object class ke paas kuch basic methods hote hain, jaise: __str__(), __repr__(), __eq__(), __hash__(), __init__(), __new__(), __format__(), __sizeof__() etc. which also doesn't have 'eat()'