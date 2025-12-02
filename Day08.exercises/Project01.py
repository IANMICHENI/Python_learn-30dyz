'''
Personal Driving Eligibility Checker

Objective: Determine if a person is eligible to drive based on age, experience, and conditions.

Features:

Ask user for age, years of experience, and country.

Check if they are old enough to drive.

If eligible, check if they can get a license immediately or need to take a driving test.

Output different messages based on all conditions.
'''
# Day 08 of Learning Python
age = int(input("Enter your age: "))
experience = int(input("Enter years of driving experience: "))
country = input("Enter your country: ")

if age >= 18:
    if experience >= 2:
        print("You can get a full driving license immediately.")
    else:
        print(f"You need {2 - experience} more years of experience to get a full license.")
else:
    print(f"You are too young to drive. Wait {18 - age} more years.")

if country.lower() == "kenya" and age >= 18:
    print("You can apply for a Kenyan driving permit.")

    
