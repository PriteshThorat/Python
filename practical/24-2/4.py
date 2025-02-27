class Student:
  def __init__(self):
    print("This is a non parameterized constructor")

  def show(self, name):
    print("Hello ", name)

s1 = Student()
s1.show("Meenakshi")