# Program to find area of Rectangle.

def area(w, h):
    return w * h

width = int(input("Enter Width of Rectangle: "))
height = int(input("Enter Height of Rectangle: "))
print(f"The Area of Rectangle is {area(width, height)}")