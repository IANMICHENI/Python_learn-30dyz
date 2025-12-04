'''
Docstring for Day10.exercises.Exercise05
Simple Calculator

Task:

Create a function calculator(a, b, operation="add") that performs basic math operations.

operation can be "add", "subtract", "multiply", "divide" (default "add").

Return the result.

Handle divide-by-zero errors gracefully.
'''
# Day 10 of Learning Python
def calculator (a,b, operation="add"):
    
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            return "Error: Division by Zero!"
        return a / b
    else:
        return "Invalid Operation! Use 'Add','subtract','multiply','divide'."
    
print(calculator(10,5)) 
print(calculator(10,5, "subtract")) 
print(calculator(10,5, "divide"))
print(calculator(10,5, "multiply"))  
print(calculator(10,5, "add")) 