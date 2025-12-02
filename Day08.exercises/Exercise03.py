'''
Nested Condition – Even/Odd

Ask the user for a number and print:

"Number is positive and even"

"Number is positive and odd"

"Number is zero"

"Number is negative"
'''
# Day 08 of Learning Python
num = int(input("Enter a Number: "))

if num > 0:
    if num % 2 == 0:
        print("The number is positive and even")
    else:
        print("The number is positive and odd")
elif num < 0:
    if num % 2 == 0:
        print("The number is negative and even")
    else:
        print("The number is negative and odd")
else:
    print("The number is zero")