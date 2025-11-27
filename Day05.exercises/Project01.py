''''
Student Grades Analyzer

Objective: Build a program that manages student grades and provides analytics.

Features to implement:

Store students and their grades in lists: students = ["Alice", "Bob", "Charlie"], grades = [85, 92, 78].

Print the first, middle, and last student along with their grades.

Add a new student with a grade.

Remove a student who dropped the course.

Modify a grade if a student retakes an exam.

Calculate min, max, average, median, and range of grades.

Sort students by grades ascending and descending.

Slice top 2 and bottom 2 students.
'''
#Day 05 of Learning Python
print("---------- Student Grades Analyzer -----------")

students = ["Alice", "Bob", "Charlie"]
grades = [85, 92, 78]

#Print the first, middle, and last student along with their grades.
first_std = students[0]
middle_std = students[1]
last_std = students[-1]

first_grd = grades[0]
middle_grd = grades[1]
last_grd = grades[-1]

print(f"Name:{first_std} Grade:{first_grd}")
print(f"Name:{middle_std} Grade:{middle_grd}")
print(f"Name:{last_std} Grade:{last_grd}")

students.append("Mathew")
grades.append(88)

print(students)
print(grades)

students.remove("Bob")
print(students)

grades[1] = 96
print(grades)

max_grade = max(grades)
min_grade = min(grades)

print(max_grade)
print(min_grade)

average = sum(grades) / len(grades)
print(average)

range = max_grade - min_grade
print(range)

grades.sort()
print(grades)
grades.sort(reverse=True)
print(grades)

students[0:1]
students[2:3]

print(students)