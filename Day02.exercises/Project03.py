''' Project 4 — Magic Number Analyzer
Goal:

Ask the user for a number and analyze it in different ways: is it even/odd, positive/negative, a multiple of 5 or 10, and display all info neatly.

Step-by-Step Instructions (Plain Words)

Start a new Python file and add a comment:
"Day 2: Magic Number Analyzer — Fun Project"

Ask the user to input a number. Convert it to an integer or float.

Create boolean variables for:

Is the number even?

Is the number positive?

Is the number a multiple of 5?

Is the number a multiple of 10?

Analyze the number using arithmetic operations and booleans:

Even → number modulo 2 equals 0

Positive → number greater than 0

Multiple of 5 → number modulo 5 equals 0

Multiple of 10 → number modulo 10 equals 0

Use built-in functions:

abs() to show the absolute value

type() to show the datatype

Create a multi-line output using triple quotes. Include:

Original number

Absolute value

Whether it’s even or odd

Whether it’s positive or negative

Multiple of 5 / 10

Datatype

Print the summary neatly.

Test with different numbers, including negative, zero, decimals, and multiples of 5/10.'''

# Day 2: Magic Number Analyzer — Fun Project
number = float(input("Enter a number: "))

is_even = number % 2 == 0
is_positive = number > 0
is_multiple_of_5 = number % 5 == 0
is_multiple_of_10 = number % 10 == 0

even_odd = "Even" if is_even else "Odd"
pos_neg = "Positive" if is_positive else "Negative"

abs_value = abs(number)
type_value = type(number)

Analyzer = f'''
========== Magic Number Analyzer ==========
Original Number: {number}      
Absolute Value:  {abs_value}
Datatype:        {type_value}
-------------------------
Even Or Odd Number:      {even_odd}
Positive or Negative:    {pos_neg}
Multiple of 5:           {is_multiple_of_5}
Multiple of 10:          {is_multiple_of_10}
===========================================
'''

print(Analyzer)

