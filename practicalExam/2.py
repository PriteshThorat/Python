# To find whether a number is even or odd.

def isEvenOdd(n):
    if (n % 2 == 0):
        return "The Given Number is Even."
    else:
        return "The Givem Number is Odd."
    
num = int(input("Enter the Number: "))
print(isEvenOdd(num))