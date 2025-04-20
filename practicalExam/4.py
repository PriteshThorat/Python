# Program to find out the reverse of the given number.

def reverseNum(n):
    if (n >= 0):
        return int(str(n)[::-1])
    else:
        return -int(str(-n)[::-1])

num = int(input("Enter a Number: "))
print(f"The Reverse of {num} is {reverseNum(num)}")