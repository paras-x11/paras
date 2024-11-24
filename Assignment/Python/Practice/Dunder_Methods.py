# Special Method - Magic Method - Dunder Methods

class Employee:
  def __init__(self, name):
    self.name = name

  def __len__(self):
    i = 0
    for c in self.name:
      i = i + 1
    return i

  def __str__(self):
    return f"The name of the employee is {self.name} str"
    
  def __repr__(self):
    return f"Employee('{self.name}')"

  def __call__(self):
    print("Hey I am good")


e = Employee("Paras")
# print(e.name)

print(len(e))       # internally call e.__len__()
print(str(e))       # internally call e.__len__()
print(repr(e))      # internally call e.__len__()
e()                 # internally call e.__len__()