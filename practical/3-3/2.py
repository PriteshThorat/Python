class Father:
  def display1(self):
    print("Father")

class Mother:
  def display2(self):
    print("Mother")

class Child(Father, Mother):
  def display3(self):
    print("Child")

obj = Child()
obj.display1()
obj.display2()
obj.display3()