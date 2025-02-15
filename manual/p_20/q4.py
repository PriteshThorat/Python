class StringManipulator:
  def __init__(self):
      self.text = ""

  def get_String(self):
      self.text = input("Enter a string: ")

  def print_String(self):
      print(self.text.upper())

# Example usage
obj = StringManipulator()
obj.get_String()  # User inputs a string
obj.print_String()  # Prints the uppercase version