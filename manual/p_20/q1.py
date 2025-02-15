class Power:
  def my_pow(self, x, n):
      # Base case: Any number raised to the power 0 is 1
      if n == 0:
          return 1
      # If exponent is negative, convert it to positive and take reciprocal
      if n < 0:
          return 1 / self.my_pow(x, -n)
      # If exponent is even, use (x^n = (x^(n/2))^2) for efficiency
      if n % 2 == 0:
          half_pow = self.my_pow(x, n // 2)
          return half_pow * half_pow
      # If exponent is odd, multiply once with base
      else:
          return x * self.my_pow(x, n - 1)

# Example usage
power_obj = Power()
print(power_obj.my_pow(2, 5))   # Output: 32
print(power_obj.my_pow(3, -2))  # Output: 0.1111 (approx 1/9)