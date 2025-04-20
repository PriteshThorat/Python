# Program to find factorial of a given number.

def fact(n):
    if (n <= 1):
        return 1
    
    return n * fact(n-1)

num = int(input("Enter a Positive Number: "))

print(f"The Factorial of {num} is {fact(num)}")