class Grandfather:
  def display1(self):
    print("Grandfather")

class Father(Grandfather): 
  def display2(self):
    print("Father")

class Son(Father):
  def display3(self):
    print("Son")

obj = Son()
obj.display1()
obj.display2()
obj.display3()