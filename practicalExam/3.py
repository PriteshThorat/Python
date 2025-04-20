# To check the largest number among the three numbers.

def largest(n1, n2, n3):
    if (n1 > n2 and n1 > n2):
        return n1
    elif (n2 > n1 and n2 > n3):
        return n2
    else:
        return n3
    
a = int(input("Enter the First Number: "))
b = int(input("Enter the Second Number: "))
c = int(input("Enter the Third Number: "))

print(f"The Largest Number among {a}, {b} and {c} is {largest(a, b, c)}")