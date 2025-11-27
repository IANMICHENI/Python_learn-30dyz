'''  
Full Stack Skill Tracker

Objective: Track and manage full-stack developer skills using lists.

Features to implement:

Start with front_end and back_end lists and join them into full_stack.

Insert new skills like Python, SQL, or Redux at appropriate positions.

Remove outdated skills.

Count occurrences of a particular skill.

Reverse the skills list and sort alphabetically.

Slice to get front-end and back-end subsets.

Copy the list for backup before making changes.

Join all skills into a single string for printing a resume-ready list.
'''
#Day 05 of Learning Python

print("============== Full Stack Skill Tracker ==============")

front_end = ['HTML', 'CSS', 'JS', 'React']
back_end = ['Node', 'Express', 'MongoDB']

full_stack = front_end + back_end
print(full_stack)

backup_stack = full_stack.copy()

full_stack.insert(0,'Redux')
full_stack.insert(1,'Python')

full_stack.append('SQL')
print(full_stack)

if 'Express' in full_stack:
    full_stack.remove('Express')
print(full_stack)

react_count = full_stack.count('React')
print(react_count)

full_stack.reverse()
print(full_stack)

full_stack.sort()
print(full_stack)

front_end_skills = full_stack[len(front_end)]
back_end_skills = full_stack[len(front_end):]
print(front_end_skills)
print(back_end_skills)

resume_skills = " | ".join(full_stack)
print(resume_skills)
