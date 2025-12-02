'''
Student Grading System

Objective: Assign letter grades and give personalized feedback based on score ranges.

Features:

Ask user for score (0-100).

Determine grade using if-elif-else:

80-100 → A

70-79 → B

60-69 → C

50-59 → D

0-49 → F

Provide personalized messages:

Pass/Fail

Honors if score ≥ 90
'''
# Day 08 Of Learning Python
score = int(input("Enter student's score (0-100): "))

if 80 <= score <= 100:
    grade = "A"
    message = "Excellent work! You got an A."
elif 70 <= score <= 79:
    grade = "B"
    message = "Good job! You got a B."
elif 60 <= score <= 69:
    grade = "C"
    message = "You passed with a C."
elif 50 <= score <= 59:
    grade = "D"
    message = "You barely passed with a D."
elif 0 <= score < 50:
    grade = "F"
    message = "You failed. Try harder next time."
else:
    grade = None
    message = "Invalid score entered."

print(f"Grade: {grade}")
print(message)

if grade == "A" and score >= 90:
    print("Congratulations! You achieved Honors.")
