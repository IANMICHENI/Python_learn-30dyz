'''
EXERCISE 1 — String Building & Transformations

Create these strings:

"Thirty"

"Days"

"Of"

"Python"

Task:

Combine them into one sentence.

Create another sentence by joining:

"Coding", "For", "All".

Store "Coding For All" in a variable called company.

Print:

company

length of company

company in UPPERCASE

company in lowercase

company capitalized

company in title case

company with swapped case
'''
#Day 04 of learning python

num = "Thirty"
time = "Days"
what = "Of"
learn = "Python"

sentence = num+ " " +time+ " " +what+ " " +learn
print(sentence)

add_1 = "Coding"
add_2 = "For"
add_3 = "All"

company = add_1+ " " +add_2+ " " +add_3

sentence_2 = sentence+ " " +company
print(sentence_2)

length = len(company)
print(length)

print(company.upper())
print(sentence.upper())
print(sentence_2.upper())

print(company.lower())
print(sentence_2.lower())

print(company.capitalize())
print(sentence.capitalize())
print(sentence_2.capitalize())

print(sentence_2.replace("Thirty","Napenda Ugali"))
print(sentence_2.title())
print(company.swapcase())

print(sentence_2[2])
print(sentence_2[4])
print(sentence [-2])
print(company [2])




