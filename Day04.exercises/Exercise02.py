''''
EXERCISE 2 — Slicing, Searching & Replacing

Using the variable:
company = "Coding For All"

Perform:

Slice out the word "Coding".

Check if "Coding" exists in company (using in).

Replace "Coding" with "Python".

Replace "Everyone" with "All" in:
"Python for Everyone".

Split "Coding For All" into a list.

Split:
"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
into a list using a comma.
'''
#Day 4 learning Python
company = "Coding For All"
print(company[0:6])

exist = "Coding" in company
print(exist)

print(company.replace("Coding","Python"))
print(company.replace("All","Everyone"))
print(company.split())

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
companies_list = companies.split(",")
print(companies_list)


