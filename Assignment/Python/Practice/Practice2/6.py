
# ### 📌 Object-Oriented Programming



# 29. Implement a decorator to log function execution.
def extra_func(func):
    print("before main func")
    func()
    print("after main func")

@extra_func
def main_func():
    print("Main func workinhg")



# 30. Use `*args` and `**kwargs` in a sample function.
def avg(*args):
    sum = 0
    for n in args:
        sum += n
    return sum // len(args)

average = avg(10,20,30,40,50,6)
print(average)


# 31. Create a class for `BankAccount` with deposit and withdraw.
class BankAccount():
    def __init__(self, b):
        self.balance = b
    
    def deposit(self, amt):
        self.balance += amt
        return f"{amt} deposited succesfully\nNew balance is: {self.balance}"

    def withdraw(self, amt):
        if amt > self.balance:
            return f"Not Enough Balance.."
        else:
            self.balance -= amt
            return f"{amt} withdrawed succesfully\nNew balance is: {self.balance}"
        
    def get_balance(self):
        return f"Balance is: {self.balance}"
        
paras = BankAccount(50000)
print(paras.deposit(50000))
print(paras.withdraw(5000))
print(paras.get_balance())
print(paras.withdraw(25000))
print(paras.get_balance())



# 32. Implement inheritance: `Vehicle -> Car, Bike`.
class Vehicle():
    def __init__(self, brand, speed, wheels):
        self.brand = brand
        self.speed = speed
        self.wheels = wheels

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Speed: {self.speed} km/h")
        print(f"Wheels: {self.wheels}")

class Car(Vehicle):
    def __init__(self, brand, speed, wheels, no_of_doors):
        super().__init__(brand, speed, wheels)
        self.no_of_doors = no_of_doors

    def display_info(self):
        super().display_info()
        print(f"No of doors: {self.no_of_doors}")

class Bike(Vehicle):
    def __init__(self, brand, speed, wheels, type):
        super().__init__(brand, speed, wheels)
        self.type = type

    def display_info(self):
        super().display_info()
        print(f"Type: {self.type}")

c = Car("Toyota", 120, 4, 4)
b = Bike("Yamaha", 90, 2, "Sport")

print("Car Info:")
c.display_info()

print("\nBike Info:")
b.display_info()


# 33. Use @property decorators for a class.
# The @property decorator in Python makes a method behave like an attribute — so you can access it without parentheses (), just like you'd access a variable.
class Person:
    def __init__(self, name):
        self._name = name  # underscore means "protected"

    @property
    def name(self):
        print("Getting name...")
        return self._name

    @name.setter
    def name(self, value):
        print("Setting name...")
        self._name = value

    @name.deleter
    def name(self):
        print("Deleting name...")
        del self._name

p = Person("Paras")

print(p.name)    # Acts like an attribute (calls getter)
p.name = "Dev"   # Calls setter
del p.name       # Calls deleter


# 34. Overload operators using magic methods (`__add__`, `__str__`).
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # Overloading the str() function (for printing)
    def __str__(self):
        return f"Point({self.x}, {self.y})"


p1 = Point(2, 3)
p2 = Point(5, 7)

p3 = p1 + p2

print(p3)  # Output: Point(7, 10)



# 35. Design a simple library management system with classes.