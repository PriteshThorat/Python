class Student:
  def __init__(self, name="Unknown", age=0):
      self.name = name
      self.age = age

  def display(self):
      print(f"Student Name: {self.name}, Age: {self.age}")

# Creating objects with different arguments
s1 = Student()              # Uses default values
s2 = Student("Alice")       # Uses default age
s3 = Student("Bob", 22)     # Passes both values

s1.display()  # Output: Student Name: Unknown, Age: 0
s2.display()  # Output: Student Name: Alice, Age: 0
s3.display()  # Output: Student Name: Bob, Age: 22
