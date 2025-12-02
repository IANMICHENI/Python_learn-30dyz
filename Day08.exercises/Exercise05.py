''' 
Skill Checker

Given a dictionary:

person = {
    'first_name': 'Asabeneh',
    'skills': ['JavaScript', 'React', 'Node', 'Python']
}


Write a program to check:

If person has 'Python' skill → print "Knows Python"

If skills contain only 'JavaScript' and 'React' → print "Front-end Developer"

If skills contain 'Node', 'Python', 'MongoDB' → print "Back-end Developer"

If skills contain 'React', 'Node', 'MongoDB' → print "Full-stack Developer"

Otherwise → print "Unknown Title"
'''
# Day 08 Of Learning Python
person = {
    'first_name': 'Asabeneh',
    'skills': ['JavaScript', 'React', 'Node', 'Python']
}

skills = person['skills']

if 'Python' in skills:
    print("Knows Python")

if set(skills) == {'JavaScript', 'React'}:
    print("Front-end Developer")
elif set(['Node', 'Python', 'MongoDB']).issubset(skills):
    print("Back-end Developer")

elif set(['React', 'Node', 'MongoDB']).issubset(skills):
    print("Full-stack Developer")
else:
    print("Unknown Title")

    