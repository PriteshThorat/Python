class BankAccount:
  def __init__(self, account_holder, balance):
      self.account_holder = account_holder  # Public attribute
      self.__balance = balance  # Private attribute (data hiding)

  def deposit(self, amount):
      if amount > 0:
          self.__balance += amount
          print(f"Deposited {amount}. New balance: {self.__balance}")
      else:
          print("Deposit amount must be positive.")

  def withdraw(self, amount):
      if 0 < amount <= self.__balance:
          self.__balance -= amount
          print(f"Withdrawn {amount}. Remaining balance: {self.__balance}")
      else:
          print("Invalid withdrawal amount or insufficient balance.")

  def get_balance(self):  # Public method to access private data
      return self.__balance

# Creating an account object
account = BankAccount("John Doe", 1000)

# Accessing public attribute
print("Account Holder:", account.account_holder)

# Accessing private attribute (will raise an error)
# print(account.__balance)  # Uncommenting this will cause an AttributeError

# Using public methods to interact with private data
account.deposit(500)
account.withdraw(300)

# Accessing private variable using a getter method
print("Final Balance:", account.get_balance())