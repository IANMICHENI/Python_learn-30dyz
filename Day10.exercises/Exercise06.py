'''
Apply Multiple Functions

Task:

Create at least two functions: square(n) and cube(n) that return n^2 and n^3.

Create a function apply_functions(func_list, *args) that:

Accepts a list of functions (func_list)

Accepts any number of arguments (*args)

Returns a dictionary where keys are function names and values are lists of results after applying the function to each argument.
'''

def square(n):
    return n * n

def cube(n):
    return n * n * n

def apply_functions(func_list, *args):
    results = {}
    for func in func_list:
        results[func.__name__] = [func(arg) for arg in args] 
    return results
    
functions = [square, cube]
print(apply_functions(functions, 1,2,3))
print(apply_functions(functions, 4,5,6))

