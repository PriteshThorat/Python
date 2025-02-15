class Degree:
  def getDegree(self):
      print("I got a degree")

class Undergraduate(Degree):
  def getDegree(self):
      print("I am an Undergraduate")

class Postgraduate(Degree):
  def getDegree(self):
      print("I am a Postgraduate")

# Creating objects of each class
d = Degree()
ug = Undergraduate()
pg = Postgraduate()

# Calling getDegree() method for each class
d.getDegree()   # Output: I got a degree
ug.getDegree()  # Output: I am an Undergraduate
pg.getDegree()  # Output: I am a Postgraduate