'''  
Age Checker

Ask the user for their age and print:

"You are old enough to drive" if age ≥ 18

"You need X more years to learn to drive" if age < 18
'''
# Day 08 of Learning Python
age = int(input("Enter Your Age: "))

if age >= 18:
    print("You are Old Enough To Drive")
elif age < 18:
    print("You need X more years to learn to drive")