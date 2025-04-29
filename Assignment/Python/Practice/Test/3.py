# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Question 3:
# Create a base class Employee with a method get_salary().
# Then create a subclass Manager that extends this method to include a bonus.

# class Employee:
#     def __init__(self, name, salary): ...
#     def get_salary(self): ...

# class Manager(Employee):
#     def __init__(self, name, salary, bonus): ...
#     def get_salary(self):  # override and include bonus


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Employee:
    def __init__(self, name, salary): 
        self._name = name
        self._salary = salary
        print(f"\n-> Object '{self._name}' Created")

    def get_salary(self):
        print(f"{self._name}'s salary is: {self._salary}")
        return self._salary

    def set_new_salary(self, amt):
        self._salary = amt
        print(f"{self._name}'s new salary is set to: {self._salary}")
        return self._salary


class Manager(Employee):
    def __init__(self, name, salary, bonus): 
        super().__init__(name, salary)
        self._bonus = bonus

    def get_salary(self):
        total_salary = self._salary + self._bonus
        print(f"{self._name}'s total salary (salary + bonus) is: {total_salary}")
        return total_salary


e = Employee('pavan', 20000)
e.get_salary()
e.set_new_salary(30000)
print("New Salary: ", e.get_salary())

print("=================================================================")

m = Manager('paras', 50000, 5000)
m.get_salary()
m.set_new_salary(70000)
print("New Salary: ", m.get_salary())




