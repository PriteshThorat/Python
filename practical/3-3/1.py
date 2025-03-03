'''
Syntax:-

class A:
#Properities of class A

class B(A):
#Properities of class B
'''

class Vehicle:
  name = "Maruti"

  def display(self):
    print("Name = ", self.name)

class Category(Vehicle):
  price = 2000

  def disp_price(self):
    print("Price = ", self.price)

car = Category()
car.display()
car.disp_price()