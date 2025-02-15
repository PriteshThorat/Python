class IntegerToRoman:
  def int_to_roman(self, num):
      # Define Roman numeral mappings
      val = [
          (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
          (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
          (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
      ]

      roman = ""  # Result string
      for value, symbol in val:
          while num >= value:
              roman += symbol
              num -= value
      return roman

# Example usage
converter = IntegerToRoman()
print(converter.int_to_roman(3549))  # Output: "MMMDXLIX"
print(converter.int_to_roman(1994))  # Output: "MCMXCIV"
print(converter.int_to_roman(58))    # Output: "LVIII"