'''
Student Grades Tracker

Objective: Track students’ grades and perform analytics.

Features:

Store students and grades as a dictionary: {'Alice': 85, 'Bob': 92}

Add new students with grades.

Modify grades if students retake exams.

Remove students who leave the class.

Calculate average, min, max grades.

List students in ascending or descending order of grades.
'''
#Day 07 Of Learning Python
grades = {'Alice': 85, 'Bob': 92 }

grades["Mwangii"] = 76
grades["Kimani"] = 86

grades['Mwangii'] = 100

grades.pop('Alice')
print(grades)

all_grades = grades.values()
print(all_grades)

min_grade = min(all_grades)
print(min_grade)

max_grades = max(all_grades)
print(max_grades)

average = sum(all_grades) / len(all_grades)
print(f"{average:.2f}")

ascending = dict(sorted(grades.items(), key=lambda item: item[1]))
print(f"Ascending order:{ascending}")

descending = dict(sorted(grades.items(), key=lambda item: item[1], reverse=True))
print("Descending order:", descending)
