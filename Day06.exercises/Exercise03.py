'''  
Full-Stack Skill Tracker

Objective: Track and analyze developer skills using tuples and sets.

Tasks:

Create tuples for front_end and back_end skills.

front_end = ('HTML', 'CSS', 'JS', 'React')
back_end = ('Node', 'Python', 'SQL')


Join the tuples to form full_stack.

Convert full_stack to a set to remove duplicates.

Add new skills like 'Redux', 'TypeScript' using set operations.

Remove outdated skills like 'CSS'.

Slice the original tuple to get front-end and back-end lists.

Count how many times a particular skill appears in the tuple.

Perform set operations with another developer’s skill set:

other_dev = {'HTML', 'Python', 'Django', 'React'}


Find common skills (intersection)

Find unique skills (symmetric difference)

Print the final sorted skill set ready for a resume.
'''
#Day 06 of learning Python
front_end = ('HTML', 'CSS', 'JS', 'React')
back_end = ('Node', 'Python', 'SQL')

other_dev = {'HTML', 'Python', 'Django', 'React'}


full_stack = front_end + back_end
print(full_stack)

set_a = set(full_stack)
set_b = set(other_dev)

full_stack_set = set(full_stack)

set_a.update(["Redux","Typescript"])

print(set_a)
set_a.discard("CSS")
print(set_a)

front_end_list = full_stack[:len(front_end)]
back_end_list = full_stack[len(front_end):]

print("Front-end List:", front_end_list)
print("Back-end List:", back_end_list)

count = full_stack.count("Python")
print(count)

inter = set_a.intersection(set_b)
print(inter)

sym_diff =set_a.symmetric_difference(set_b)
print(sym_diff)

sorted_skill = tuple(sorted(full_stack_set))
print(sorted_skill)