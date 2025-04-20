# Program for hierarchical inheritance.

class Base:
    def __init__(self):
        print("Hello from Base Class Constructor")
    
class Derived1(Base):
    def __init__(self):
        super().__init__()
        print("Hello from Derived1 Class Constructor")

class Derived2(Base):
    def __init__(self):
        super().__init__()
        print("Hello from Derived2 Class Constructor")

class Derived3(Base):
    def __init__(self):
        super().__init__()
        print("Hello from Derived3 Class Constructor")

print("Creating an Object of Derived1 Class")
obj1 = Derived1()

print("\nCreating an Object of Derived2 Class")
obj2 = Derived2()

print("\nCreating an Object of Derived3 Class")
obj3 = Derived3()