# Python program to sum all the items in a list.
from functools import reduce

l = [1, 2, 3, 4, 5, 6, 7, 8]
sum = reduce(lambda a, b : a + b, l)

print(f"The Sum of {l} is {sum}")