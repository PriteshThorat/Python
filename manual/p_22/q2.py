class Shape:
  def area(self, length, breadth=None):
      if breadth is None:  # If only one argument is given, it's a square
          print(f"Area of Square: {length * length}")
      else:  # If two arguments are given, it's a rectangle
          print(f"Area of Rectangle: {length * breadth}")

# Creating an object of Shape class
shape = Shape()

# Calculating areas
shape.area(5)        # Square (side = 5)
shape.area(10, 20)   # Rectangle (length = 10, breadth = 20)