'''
✅ PROJECT 1: Geometry Master Calculator

Covers: triangle area, triangle perimeter, rectangle area/perimeter, circle area/circumference, height/age variables, floats, ints.

Instructions (Write these as code):

Ask the user to enter:

age (int)

height (float)

radius of a circle

base + height of a triangle

sides a, b, c of another triangle

length + width of a rectangle

Compute:

triangle area

triangle perimeter

rectangle area

rectangle perimeter

circle area

circle circumference

Display ALL results in a clean multi-line format using """ """.

Use:

ints

floats

arithmetic

variables
'''
#Day 3 :Python is Awesome

age = int(input("Enter Your Age: "))
height = int(input("Enter Height: "))
radius = int(input("Enter Radius: "))

base_triangle = int(input("Enter Base of the Triangle: "))
height_triangle = int(input("Enter Height of the Triangle: "))

#Triangle
side_a = int(input("Enter Side A: "))
side_b = int(input("Enter Side B: "))
side_c = int(input("Enter Side C: "))

#Rectangle
length_rectangle = int(input("Enter Length of Rectangle: "))
width_rectangle = int(input("Enter Width of Rectangle: ")) 

#Compute
triangle_area = 0.5 * base_triangle * height_triangle
triangle_perimeter = side_a + side_b + side_c
rectangle_area = length_rectangle * width_rectangle
rectangle_perimeter = 2 * (length_rectangle + width_rectangle)
circle_area = 3.14 * radius * radius
circle_circumference = 2 * 3.14 * radius 

display = (F'''
====================== RESULTS ============================
           Age: {age}
    
    Circle Area:{circle_area}
    Circle Circumference:{circle_circumference}
    Triangle Perimeter: {triangle_perimeter}
    Triangle Area: {triangle_area}
    Rectangle Area: {rectangle_area}
    Rectangle Perimeter: {rectangle_perimeter}
    
    ''')
print(f"{display}")