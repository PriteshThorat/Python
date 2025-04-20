# Python program to multiplies all the items in a list.

from functools import reduce

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

mul = reduce(lambda a, b : a * b, list)
print(f"The Multiplication of {list} is {mul}")