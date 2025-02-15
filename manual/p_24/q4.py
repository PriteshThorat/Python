class Person:
  def __init__(self, name, age):
      self.name = name
      self.age = age

  def display_person(self):
      print(f"Name: {self.name}")
      print(f"Age: {self.age}")

class Student(Person):
  def __init__(self, name, age, roll_no, grade):
      super().__init__(name, age)  # Inheriting from Person
      self.roll_no = roll_no
      self.grade = grade

  def display_student(self):
      self.display_person()  # Calling parent class method
      print(f"Roll Number: {self.roll_no}")
      print(f"Grade: {self.grade}")

# Child class inheriting from Student
class CollegeStudent(Student):
  def __init__(self, name, age, roll_no, grade, course):
      super().__init__(name, age, roll_no, grade)  # Inheriting from Student
      self.course = course

  def display_info(self):
      self.display_student()  # Calling parent class method
      print(f"Course: {self.course}")

# Creating an object of CollegeStudent
student1 = CollegeStudent("Alice", 20, "CS101", "A", "Computer Science")

# Displaying student details
student1.display_info()