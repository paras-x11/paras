#  13) Write a Python program to show single inheritance. 

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog barks")

    def sleep(self):
        print("dog is sleeping")

dog = Dog()
dog.speak()
dog.sleep()


# Constructor
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal created: {self.name}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # No need to pass 'self', just 'name'
        self.breed = breed
        print(f"Dog created: {self.name}, {self.breed}")

animal = Animal("dog")
dog = Dog("Buddy", "Golden Retriever")
