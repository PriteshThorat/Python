class Student:
  def __init__(self, name):
    print("This is a parameterized constructor")
    self.name = name

  def show(self):
    print("Hello ", self.name)

s1 = Student("Meenakshi")
s1.show()