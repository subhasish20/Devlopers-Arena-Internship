# Create a function that calculates area of rectangle


def AreaOfRectangle(length, widht):
    return length * widht

length = float(input("Enter the length of the rectangle :"))
width = float(input("Enter the width of the rectangle :"))

area = AreaOfRectangle(length, width)

print(f"The are of the rectangle is {area}")