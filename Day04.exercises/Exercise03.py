''''
EXERCISE 3 — Character Indexing & Acronyms

Using company = "Coding For All":

Print:

first character

last character

10th character

Create acronyms for:

"Python For Everyone"

"Coding For All"

Use .index() to find:

position of "C"

position of "F"

Use .rfind() to find last position of "l" in:
"Coding For All People"
'''
#Day04 of learning python
company = "Coding For All"
print(company[0])
print(company[-1])
print(company[9])

position = company.index('C')
print(position)

position = company.index('F')
print(position)

company_2 = "Coding For All People"
position_2 = company_2.rfind('l')
print(position_2)

#Acronym
company_Acr = " ".join([word[0].upper() for word in company.split()])
print(company_Acr)
company_Acron = " ".join([word[0].upper() for word in company_2.split()])
print(company_Acron)