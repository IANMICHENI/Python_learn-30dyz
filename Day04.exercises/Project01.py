''' Project 1 — Personal Info Formatter

Goal: Use strings, concatenation, formatting, and escape sequences to display user info neatly.

Instructions:

Ask the user for:

Full name

Age

Country

City

Favorite programming language

Hobby

Create a multi-line string that formats the information using:

\n for new lines

\t for aligning columns

Triple quotes for readability

Transform the string with:

Uppercase

Lowercase

Title case

Swapcase

Replace the hobby with another string (use .replace())

Print a summary using f-strings, including:

Name in uppercase

Age

Country and city

Favorite language and hobby
Project 1 — Personal Info Formatter

Goal: Use strings, concatenation, formatting, and escape sequences to display user info neatly.

Instructions:

Ask the user for:

Full name

Age

Country

City

Favorite programming language

Hobby

Create a multi-line string that formats the information using:

\n for new lines

\t for aligning columns

Triple quotes for readability

Transform the string with:

Uppercase

Lowercase

Title case

Swapcase

Replace the hobby with another string (use .replace())

Print a summary using f-strings, including:

Name in uppercase

Age

Country and city

Favorite language and hobby 
''' 
#Day 4 of Python Learning
name = input("Enter Full Name: ")
age = int(input("Enter Your Age: "))
country = input("Enter Your Country: ")
city = input("Enter Your City: ")
favorite_programming_language = input("Enter Favourite Programming Language:  ")
hobby = input("Enter Your Favourite Hobby: ")

summary = f'''  
========== INFO ==========
Name: {name}
Age: {age}
Country: {country}
City: {city}
Favourite Programming Language: {favorite_programming_language}
Hobby: {hobby}
==========================
'''

print("UPPERCASE:\n", summary.upper())
print("LOWERCASE:\n", summary.lower())
print("TITLE CASE:\n", summary.title())
print("SWAPCASE:\n", summary.swapcase())

new_hobby = hobby.replace(hobby, "Maziwa")
summary_replaced = summary.replace(hobby, new_hobby)
print("REPLACED HOBBY:\n", summary_replaced)

f_summary = f"""
========== PERSONAL SUMMARY ==========
Name: {name.upper()}
Age: {age}
Location: {city}, {country}
Favorite Language: {favorite_programming_language}
Hobby: {hobby}
======================================
"""
print(f_summary)