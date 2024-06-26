#W1 Assignment Declan Bartel

# CS 16X Git Assignment

# Project requires TWO functions:
# 1. rect_area (length, width) which will return the area of a rectangle
# 2. rect_solid_area (length, width, height) which will return the area of a solid rectangular object

# The following four lines are just there to make the code work without errors until functions are added
#def rect_solid_area(x, y, z):
#    return 1
#length = 1; width = 1; height = 1
#rect_solid_area (length, width, height)

# Request the dimension of a solid rectangular object
length = int(input("Enter the length of the the object as in integer: "))
width = int(input("Enter the width of the the object as in integer: "))
height = int(input("Enter the height of the the object as in integer: "))

def rect_area(length, width):
    return length * width

def rect_solid_area(length, witdth, height):
    return 2*(length*width) + 2*(witdth*height) + 2*(length*height)

surface_area = rect_solid_area(length, width, height)

print("Length = ", length, "Width = ", width, "Height = ", height)
print(f"The area of the rectangle is {rect_area(length, width)}")
print("Total Surface Area = ", surface_area)