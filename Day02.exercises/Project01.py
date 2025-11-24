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

Run your program and make sure it prints everything neatly. '''

# "Day 2: 30 Days of Python Programming — Personal Profile Generator"

first_name = "Ianoh"
last_name = "Mwenda"
full_name = first_name + " " + last_name

country = "Kenya"
city = "Nairobi"
age = 21
year = 2025

is_married = False
is_true = True
is_light_on = True

hobby, favourite_food, favourite_color = 'Swimming','Ugali' ,'Blue'

profile = (f'''
============ MY PROFILE CARD ============
Fullname: {full_name}
Country: {country}
City:{city}
Age:{age}
Year:{year}

Married:{is_married}
Truth Value:{is_true}
Lights On:{is_light_on}

Other Info:
Hobby:{hobby}
Favourite Food:{favourite_food}
Favourite Color:{favourite_color}

=========================================
        
    ''')
print(f"{profile}")