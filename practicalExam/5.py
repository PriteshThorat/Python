# Program to check whether the entered number is prime or not.

def isPrime(n):
    if n <= 1:
        return "Not a Prime"
    
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0:
            return "Not a Prime"
        
    return "a Prime"

num = int(input("Enter a Number: "))

print(f"The {num} is {isPrime(num)} Number")