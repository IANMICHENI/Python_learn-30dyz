''' 
Number Set Analyzer

Objective: Perform numeric set operations.

Tasks:

Create sets:

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}


Perform and print:

Union

Intersection

Difference (A-B, B-A)

Symmetric difference

Check if A is subset of B

Check if B is superset of A

Check if A and B are disjoint
'''
#Day 06 Of Learning Python


A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

union_result = A.union(B)
print(union_result)

inter = A.intersection(B)
print(inter)

sym_diff = A.symmetric_difference(B)
print(sym_diff)

is_a_subset_b = A.issubset(B)
print(is_a_subset_b)

is_b_superset_a = B.issuperset(A)
print(is_b_superset_a)

is_a_b_disjoint = A.isdisjoint(B)
print(is_a_b_disjoint)

