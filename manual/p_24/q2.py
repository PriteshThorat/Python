class Student:
  def __init__(self, name, roll_no, grade):
      self.name = name
      self.roll_no = roll_no
      self.grade = grade

class Details(Student):
  def display_info(self):
      print("\nStudent Information:")
      print(f"Name: {self.name}")
      print(f"Roll Number: {self.roll_no}")
      print(f"Grade: {self.grade}")

# Taking input from user
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
grade = input("Enter Grade: ")

# Creating object of Details class
student1 = Details(name, roll_no, grade)

# Displaying student details
student1.display_info()