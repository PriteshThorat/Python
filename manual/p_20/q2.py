class StringReverser:
  def reverse_words(self, text):
      # Split the text into words, reverse the order, and join them back
      return ' '.join(text.split()[::-1])

# Example usage
reverser = StringReverser()
print(reverser.reverse_words("Hello World Python"))  # Output: "Python World Hello"
print(reverser.reverse_words("ChatGPT is amazing"))  # Output: "amazing is ChatGPT"