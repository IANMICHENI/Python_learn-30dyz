'''
PROJECT 4 — Ultimate Personal Analyzer
Goal:

Create a program that asks the user for personal info and preferences, does numeric and string analysis, and prints a full report.

Step-by-Step Instructions (Plain Words)

Start a new Python file and add a comment:

Ask the user to enter:

Name

Age

Height in meters

Favorite number

A favorite word or hobby

Calculate numeric stuff:

Convert age to float and string

Square the favorite number

Check if the favorite number is even or odd

Calculate string stuff:

Length of the name and hobby

Convert lengths → float → string

Check if "a" appears in both name and hobby

Check if the hobby starts with the same letter as the name

Create boolean checks:

Is the person adult? (age ≥ 18)

Is favorite number divisible by 5?

Falsy comparison example: (name length > hobby length AND name length < hobby length)

Display everything neatly using a formatted multi-line string
'''
# Day 3: Ultimate Personal Analyzer
Name = input("Enter Your Name: ")
Age = int(input("Enter Your Age: "))
Height_in_meters = float(input("Enter Height in Meters: "))
Favorite_number = int(input("Enter Favourite Number: "))
Favorite_word = input("Enter Favourite Word: ")
Favorite_hobby = input("Enter Favourite Hobby: ")

Age_float = float(Age)
Age_str = str(Age_float)

FavNum_squared = Favorite_number ** 2
is_FavNum_even = Favorite_number % 2 == 0

name_len = len(Name)
hobby_len = len(Favorite_hobby)

name_len_float = float(name_len)
hobby_len_float = float(hobby_len)

name_len_str = str(name_len_float)
hobby_len_str = str(hobby_len_float)

a_in_both = "a" in Name.lower() and "a" in Favorite_hobby.lower()
same_start_letter = Name[0].lower() == Favorite_hobby[0].lower()

is_adult = Age >= 18
divisible_by_5 = Favorite_number % 5 == 0
falsy_check = name_len > hobby_len and name_len < hobby_len  # Always False

report = f"""
================= Ultimate Personal Analyzer =================

Name: {Name}
Age: {Age} (float: {Age_float}, str: {Age_str})
Height: {Height_in_meters} meters

Favorite Number: {Favorite_number}
Squared Favorite Number: {FavNum_squared}
Is Favorite Number Even? {is_FavNum_even}
Divisible by 5? {divisible_by_5}

Favorite Word: {Favorite_word}
Favorite Hobby: {Favorite_hobby}
Length of Name: {name_len} (float: {name_len_float}, str: {name_len_str})
Length of Hobby: {hobby_len} (float: {hobby_len_float}, str: {hobby_len_str})

Does 'a' appear in both Name and Hobby? {a_in_both}
Do Name and Hobby start with same letter? {same_start_letter}
Is user adult? {is_adult}
Falsy Check Example: {falsy_check}

================================================================
"""

print(report)


