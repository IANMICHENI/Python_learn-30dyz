'''
Exercise 5 — String Formatting & Arithmetic

Goal: Practice old-style formatting, .format(), and f-strings with numbers.

Instructions (Plain Words):

Declare two numbers: a = 8, b = 6.

Print the results of the following using all three string formatting methods:

a + b

a - b

a * b

a / b (limit to 2 decimal places)

a % b

a // b

a ** b

Print a statement using .format() about the area of a circle with radius = 10 and pi = 3.14.
Example: "The area of a circle with radius 10 is 314.00."
'''
#Day 04 Of Learning Python
a = 8
b = 6

add = a + b
subtraction = a - b
multiplication = a * b
division = a / b
modulos = a % b
power = a ** b
ddivide = a // b

print("Total is %d ." % (add))
print("The Total is {:.2f} .".format(add))
print(f"{add}")

print("Total is %d ." % (subtraction))
print("The Total is {:.2f} .".format(subtraction))
print(f"{subtraction}")

print("Total is %d ." % (multiplication))
print("The Total is {:.2f} .".format(multiplication))
print(f"{multiplication}")

print("Total is %f ." % (division))
print("The Total is {:.2f} .".format(division))
print(f"{division}") 

print("Total is %d ." % (power))
print("The Total is {:.2f} .".format(power))
print(f"{power}")

print("Total is %f ." % (ddivide))
print("The Total is {:.2f} .".format(ddivide))
print(f"{ddivide}")

radius = 10
pi = 3.14

area = pi * radius * radius

print("The area of a circle with radius {} is {:.2f}.".format(radius,area))
