# Program for Single inheritance using constructor.

class Base:
    def __init__(self):
        print("Hello from Base Class Constructor")

class Derived(Base):
    def __init__(self):
        super().__init__()
        print("Hello from Derived Class Constructor")

print("Creating Object of Derived Class")
d = Derived()