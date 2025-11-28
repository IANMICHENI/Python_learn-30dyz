'''
Student Club Membership System

Objective: Track students in different clubs and analyze memberships.

Tasks:

Create tuples for club_a and club_b with student names.

Convert tuples to sets for easy operations.

Find and print:

Students in both clubs (intersection)

Students only in club_a (difference)

All students in either club (union)

Students in either but not both clubs (symmetric difference)

Check if club_a is a superset of club_b and if club_b is a subset of club_a.

Add a new student to club_a using set operations.

Remove a student from club_b.
'''
#Day 06 of learning Python
club_a = ["Alice","John","James","Peter","Peter"]
club_b = ["Mathew","Kamau", "Lucy", "Peter", "Austin"]
students = club_a + club_b

print(students)
std_length = len(students)
print(std_length)

set_a = set(club_a)
set_b = set(club_b)

print("\n----------- INTERSECTION ---------")
inter_result = set_a.intersection(set_b)
print(inter_result)

print("\n----------- DIFFERENCE -----------")
diff_result = set_a.difference(set_b)
print(diff_result)

print("\n----------- UNION ---------")
union_result = set_a.union(set_b)
print(union_result)

print("\n------------- SYMMETRIC DIFFERENCE --------------")
sym_diff = set_a.symmetric_difference(set_b)
print(sym_diff)

print("\n----------- SUPERSET ----------")
super_sett = set_a.issuperset(set_b)
print(super_sett)

print("\n---------- ADDING ----------")
set_a.add("Mwangiiii")
print(set_a)

print("\n---------- REMOVING ----------")
set_b.discard("Mathew")
print(set_b)
