'''
Online Course Skill Analyzer

Objective: Analyze skills from multiple students in a course using tuples and sets.

Features:

Store each student’s skills as tuples, e.g.:

alice = ('Python', 'HTML', 'CSS', 'React')
bob = ('Python', 'SQL', 'Django', 'React')
charlie = ('Java', 'HTML', 'CSS')


Combine all skills into a set to see all unique skills in the course.

Count how many students know each skill.

Add a new skill for all students using update().

Remove outdated skills like 'CSS'.

Find skills common to all students (intersection).

Find skills unique to one student (difference).

Convert the final skill set back to a tuple and slice first half and second half.
'''

# Day 06 Project: Online Course Skill Analyzer

alice = ('Python', 'HTML', 'CSS', 'React')
bob = ('Python', 'SQL', 'Django', 'React')
charlie = ('Java', 'HTML', 'CSS')

all_skills = set(alice) | set(bob) | set(charlie)
print("All unique skills in course:", all_skills)

skill_to_check = 'Python'
count = sum(skill_to_check in student for student in [alice, bob, charlie])
print(f"{skill_to_check} is known by {count} students")

all_skills.update(['TypeScript', 'Redux'])

all_skills.discard('CSS')
common_skills = set(alice).intersection(bob, charlie)
print(f"Skills common to all students:{common_skills}")

unique_alice = set(alice).difference(bob, charlie)
print(f"Skills unique to Alice:{unique_alice}")

final_skills = tuple(sorted(all_skills))
mid = len(final_skills) // 2
first_half = final_skills[:mid]
second_half = final_skills[mid:]

print(f"First half of skills:{first_half}")
print(f"Second half of skills:{second_half}")
