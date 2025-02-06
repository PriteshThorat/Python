from functools import reduce

def double(x):
    return x * x

def add(x, y):
    return x + y

number1 = [1, 2, 3, 4, 5]
number2 = [6, 7, 8, 9, 10, 2]
add_no = map(add, number1, number2)
# print(list(add_no))

words = ["Hello", "World", "Python"]

uppercase_word = map(lambda word: word.upper(), words)
print(list(uppercase_word))

numbers = [1, 2, 3, 4, 5]

def multiply(x, y):
    return x * y

result = reduce(multiply, numbers)
print(result)