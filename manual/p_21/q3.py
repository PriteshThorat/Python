class Student:
  def __init__(self, name, age):  # Parameterized Constructor
      self.name = name
      self.age = age

  def display(self):
      print(f"Student Name: {self.name}, Age: {self.age}")

# Creating objects with different parameters
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

# Displaying the student details
student1.display()  # Output: Student Name: Alice, Age: 20
student2.display()  # Output: Student Name: Bob, Age: 22