'''
Basic Function with Parameters

Objective: Practice defining a function, using parameters, and returning a value.

Task:
Write a function multiply_numbers(a, b) that takes two numbers as parameters and returns their product.
'''
# Day 10 Of Learning Python
''' 
def multiply_numbers(a,b):
    return a * b
print(multiply_numbers(5,6))
'''
#Exercise 02
'''
Function with Default Parameter

Objective: Learn to use default parameter values.

Task:
Create a function greet_user(name="Guest") that prints a welcome message. If no name is provided, it should greet "Guest".
'''
    
'''

def greet_user(name="Guest"):
    print(f"Hello {name}!")
    
greet_user()

greet_user("Maasai")
'''

#Exercise 03
'''
Arbitrary Number of Arguments (*args)

Objective: Practice creating functions that accept a variable number of inputs.

Task:
Write a function average(*numbers) that takes any number of numeric arguments and returns their average. If no numbers are provided, return 0.

def num_inputs(*nums):
    total = 0
    for n in nums:
        total += n
    return total
print(num_inputs(1,2,3,4,5,6))
'''
#Exercise 04
'''
Function Returning Different Data Types

Objective: Practice returning strings, lists, and booleans from functions.

Task:

Create a function is_even(n) that returns True if the number is even, False otherwise.

Create a function first_and_last(lst) that takes a list and returns a list containing only the first and last elements.

Create a function full_name(first, last) that returns a string combining first and last name.


def full_name(first,last):
    return first+ " " +last
print(full_name(first="Ian",last="Lucas"))

def first_and_last(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return[lst[0], lst[0]]
    else:
        return [lst[0],lst[-1]]
print(first_and_last([1,2,3,4,5]))
print(first_and_last(["A","B","C"]))

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
print(is_even(10))
print(is_even(14))
print(is_even(3))
'''
# Exercise 05
'''
Function as Parameter & Arbitrary Arguments Combined

Objective: Combine multiple concepts: passing functions as arguments and handling arbitrary numbers of inputs.

Task:

Create a function square(n) that returns n*n.

Create a function apply_to_all(func, *args) that takes a function func and any number of arguments, applies func to each argument, and returns a list of results.
'''
def square(n):
    return n * n

print(square(8)) 

def apply_to_all(func, *args):
    results = []
    for arg in args:
        results.append(func(arg))
    return results 
def squared(n):
    return n * n

print(apply_to_all(squared, 2, 4))       
print(apply_to_all(square, 1, 3, 5, 7))  

    