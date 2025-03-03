class MyClass:
  counter = 0
  def __init__(self, rollNo, name):
    self.rollNo = rollNo
    self.name = name

  def display(self):
    print("Name: ", self.name)
    print("Roll No: ", self.rollNo)

obj = MyClass(1, "Meenaskshi")
obj.display()