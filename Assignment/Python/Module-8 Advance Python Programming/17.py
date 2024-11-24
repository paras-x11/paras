# 17) Write a Python program to show hybrid inheritance.

class Vehicle:
    def fuel(self):
        print("Vehicle uses fuel")

class Car(Vehicle):
    def wheels(self):
        print("Car has 4 wheels")

class Boat(Vehicle):
    def propeller(self):
        print("Boat has a propeller")

class AmphibiousCar(Car, Boat):
    def drive(self):
        print("AmphibiousCar can drive on land and water")

water_car = AmphibiousCar()
water_car.fuel()        
water_car.wheels()      
water_car.propeller()   
water_car.drive()       

