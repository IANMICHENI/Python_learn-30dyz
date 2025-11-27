'''
EXERCISE 1 — Student Database Manager

Create a Python program to manage a student list.

Requirements:

Start with this list:

students = ["Alice", "Bob", "Charlie", "Diana", "Evan"]


Print:

first, middle, last student

length of list

Modify:

change "Bob" to "Bobby"

insert "Frank" in the middle

add "Grace" at the end

Remove:

remove the first student

remove the last student

Slice:

first 2 students

last 2 students

middle students

Check:

is "Charlie" in the list?

Sort the list (ascending & descending).

Reverse the list.
'''
#Day 05 Of Learning Python

students = ["Alice", "Bob", "Charlie", "Diana", "Evan"]

first_std = "Alice"
middle_std = "Charlie"
last_std = "Evan"

first_stdd = students[0]
middle_stdd = students [2]
last_stdd = students[-1]


print(first_std)
print(middle_std)
print(last_std)
print("\n------------------------------")
#Or
print(first_stdd)
print(middle_stdd)
print(last_stdd)

length_of_list = len(students)
print(length_of_list)

print(students.insert(3, "Frank"))
print(students)
print("--------------------------------")
index = students.index("Bob")
students[index] = "Bobby"
print(students)

print(students.insert(7,"Grace"))
print(students)

print("\n----------- DELETE -------------")
print(students.pop(0))
print(students.pop(-1))
print(students)

print("\n----------- SLICE -------------")
print(students[0:2])
print(students[3:5])
print(students[3:4])

print("\n----------- Boolean -------------")
is_charlie = "Charlie" in students
print(is_charlie)

print("\n----------- SORT ASCENDING-------------")
students.sort()
print(students)

print("\n----------- SORT DESCENDING-------------")
students.sort(reverse=True)
print(students)

print("\n----------- REVERSE -------------")
students.reverse()
print(students)

