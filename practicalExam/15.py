# Program for method overriding.

class Base:
    def greet(self):
        print("Hello from Base Class Method")

class Derived(Base):
    def greet(self):
        print("Hello from Derived Class Method")

b = Base()
print("Calling greet() with Base Class Object")
b.greet()

d = Derived()
print("Calling greet() with Derived Class Object")
d.greet()