''' Project 1 — Personal Profile Generator (Build Yourself)
Instructions:

Start a new Python file and add a comment at the top saying:
"Day 2: 30 Days of Python Programming — Personal Profile Generator"

Create variables for:

first name

last name

full name (combine first and last)

country

city

age

current year

Create boolean variables for:

is married

a true/false value of your choice

a variable indicating if the light is on

Declare multiple variables on one line for things like:

hobby

favorite food

favorite color

Create a formatted multi-line profile card using triple quotes. Include all the variables you declared.

Print the profile card.

Use built-in functions:

len() to show the length of full name

type() to show the datatype of age and booleans

Run your program and make sure it prints everything neatly.

Project 2 — Smart Data Inspector (Build Yourself)
Instructions:

Start a new Python file and add a comment at the top saying:
"Day 2: Smart Data Inspector"

Ask the user for input for:

first name

last name

country

city

Ask the user for numeric input for:

age

current year
(convert these inputs to the correct numeric type)

Ask the user for yes/no or true/false inputs and convert them to boolean variables for:

is married

is the light on

Create a full name variable by combining first and last name.

Declare multiple variables in one line for things like:

favorite food

favorite movie

favorite sport

Build a multi-line summary using triple quotes and formatted strings. Include:

all user inputs

the booleans

favorite items

the datatype of full name, age, and booleans

the length of the full name and city

Print the summary neatly.

Run your program and test with different inputs to ensure everything works. '''

#Day 2: 30 Days of Python Programming — Personal Profile Generator
first_name = input("Enter your First Name: ")
last_name = input("Enter your Last Name: ")
full_name = ( first_name+ " " +last_name)

Country = input("Enter your Country: ")
City = input("Enter your city: ")
Age = input ("Enter your Age: ")
Year = int(input("Enter current Year: "))

is_married = False
is_light_on = True
is_christian = True
is_Muslim = False

hobby, favourite_food, favourite_drink, best_movie, best_sport = 'Running','Choma','Maziwa','Game','Football'

Data_inspector = (f'''
=============== Smart Data Inspector ================
Full Name:{full_name}
Age:{Age}
Country:{Country}
City:{City}

Married:{is_married}
Christian:{is_christian}

Other info:
Hobby:{hobby}
Favourite food:{favourite_food}
Favourite Drink:{favourite_drink}
Best Movie:{best_movie}
Best Sport:{best_sport}

======================================================    
    '''
)

print(f"{Data_inspector}")