'''
EXERCISE 4 — Finding, Slicing & Identifiers

Using this sentence:
"You cannot end a sentence with because because because is a conjunction"

Tasks:

Use .find() to locate first "because".

Use .rindex() to find last "because".

Slice out "because because because" from the sentence.

Check:

does company start with "Coding"?

does company end with "coding"?

Strip extra spaces from:
" Coding For All "

Check if these are valid identifiers:

"30DaysOfPython"

"thirty_days_of_python"
'''
#30 Days of Python Learning

sentence = "You cannot end a sentence with because because because is a  coding conjunction"
print(sentence.find("because"))
print(sentence.rfind("because"))       

sliced_part = sentence[sentence.find("because"):sentence.rfind("because")+len("because")]
print(sliced_part)

sentence_b = "because" in sentence
print(sentence_b)

company = "Coding" in sentence
print(company)
company = "coding" in sentence
print(company)

sentence_1 = " Coding For All "
sentence_strip = sentence_1.strip()
print(sentence_strip)

word_1 = "30DaysOfPython"
word_2 = "thirty_days_of_python"

print(word_1.isidentifier())
print(word_2.isidentifier())