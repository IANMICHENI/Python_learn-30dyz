'''
EXERCISE 2 — Full Stack Builder

You are building a full-stack developer skill list.

Requirements:

Start with:

front_end = ['HTML', 'CSS', 'JS', 'React']
back_end = ['Node', 'Express', 'MongoDB']


Join them into one list called stack using +

Copy stack into full_stack using .copy()

Insert Python, Redux, and SQL into the correct positions:

Add "Redux" after React

Add "Python" before Node

Add "SQL" at the end

Remove "CSS"

Count how many times "React" appears

Reverse the list

Sort in alphabetical order
'''
#Day 05 of learning Python

front_end = ['HTML', 'CSS', 'JS', 'React']
back_end = ['Node', 'Express', 'MongoDB']

print("=============== FULL STACK BUILD ================")

stack = front_end + back_end
print("---------- JOINING ----------")
print(stack)

full_stack = stack.copy()
print("---------- JOINING ----------")
print(full_stack)

print("---------- INSERT ----------")
front_end.insert(4,"Redux")
print(front_end)

back_end.insert(0,"Python")
print(back_end)
back_end.insert(4,"SQL")
print(back_end)

print("---------- REMOVE ----------")
front_end.remove("CSS")
print(front_end)

print("---------- COUNT ----------")
stack_count = stack.count("React")
print(stack_count)

print("---------- SORT ----------")
stack.sort()
print(stack)