'''
Personal Skill & Job Role Analyzer

Objective: Analyze a person's skills and determine their role based on predefined skill sets.

Features:

Ask user to input skills separated by comma (e.g., Python, React, Node).

Check for role:

Front-end → JS + React only

Back-end → Node + Python + MongoDB

Full-stack → React + Node + MongoDB

Otherwise → Unknown

Check if they know Python specifically.

Provide customized feedback.
'''
#Day 08 Of Learning Python
skills_input = input("Enter your skills separated by commas: ")
skills = [skill.strip().lower() for skill in skills_input.split(",")]

front_end = {'javascript', 'react'}
back_end = {'node', 'python', 'mongodb'}
full_stack = {'react', 'node', 'mongodb'}

if 'python' in skills:
    print("You know Python!")

skills_set = set(skills)

if skills_set == front_end:
    print("Front-end Developer")
elif back_end.issubset(skills_set):
    print("Back-end Developer")
elif full_stack.issubset(skills_set):
    print("Full-stack Developer")
else:
    print("Unknown Title")

if 'python' in skills_set and 'react' in skills_set:
    print("You are eligible to mentor juniors in Full-stack development.")

