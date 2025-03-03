class A:
  def display(self):
    print("This is base class")

class B(A):
  def display(self):
    print("This is derived class")

obj = B()
obj.display()