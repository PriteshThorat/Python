# Program for multilevel inheritance.

class A:
    def __init__(self):
        print("Hello from Class A, An Base Class")

class B(A):
    def __init__(self):
        super().__init__()
        print("Hello from Class B, an Middle Level Derived Class")

class C(B):
    def __init__(self):
        super().__init__()
        print("Hello from Class C, an Last Derived Class")

obj = C()