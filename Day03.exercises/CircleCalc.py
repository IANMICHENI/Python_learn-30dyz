'''
5. Circle Calculator
👉 Instructions:

Ask for radius

Use pi = 3.14

Compute:

area = pi × r × r

circumference = 2 × pi × r

Print both values
'''

radius = int(input("Enter the Radius of the Circle: "))

area = 3.14 *  radius * radius
circumference = 2 * 3.14 * radius
print("====================================================")
print(f"The Area of the Circle is: {area}")
print("-----------------------------------------------------")
print(f"The Circumference of the Circle is: {circumference}")
