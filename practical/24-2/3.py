class Person:
  def __init__(self, rollno, name, age):
    self.rollno = rollno
    self.name = name
    self.age = age
    print("Student Object is created")

p1 = Person(11, "Vijay", 15)
print("Roll No: ", p1.rollno)
print("Name: ", p1.name)
print("Age: ", p1.age)