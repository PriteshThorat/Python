class Person:
  def __init__(self, name, age):
      self.name = name
      self.age = age

  def display_person(self):
      print(f"Name: {self.name}")
      print(f"Age: {self.age}")

class Student:
  def __init__(self, roll_no, grade):
      self.roll_no = roll_no
      self.grade = grade

  def display_student(self):
      print(f"Roll Number: {self.roll_no}")
      print(f"Grade: {self.grade}")

# Child class inheriting from both Person & Student
class CollegeStudent(Person, Student):
  def __init__(self, name, age, roll_no, grade, course):
      # Initializing both parent classes
      Person.__init__(self, name, age)
      Student.__init__(self, roll_no, grade)
      self.course = course

  def display_info(self):
      self.display_person()
      self.display_student()
      print(f"Course: {self.course}")

# Creating an object of CollegeStudent
student1 = CollegeStudent("Alice", 20, "CS101", "A", "Computer Science")

# Displaying student details
student1.display_info()