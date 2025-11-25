#String Intelligence Analyzer
'''
String Intelligence Analyzer
Goal:

Analyze words and sentences for length, substrings, comparisons, booleans, and type conversions.

Step-by-Step Instructions (Plain Words)

Start a new Python file and add a comment:

# Day 3: String Intelligence Analyzer


Ask the user to enter two words:

word1

word2

Calculate the length of each word using len()

Convert the lengths:

length → float → string

Check substring presence using in:

Is "on" in both words?

Is "ing" in either word?

Check sentence for word "jargon"

Use in operator on "I hope this course is not full of jargon."

Create a falsy comparison

Compare lengths of two words with a condition that evaluates to False

Check if words start with the same letter

Print all results neatly in a multi-line block using triple quotes """ """.
'''
# Day 3: Learning pythons

word_1 = input("Enter Word 1: ")
word_2 = input("Enter Word 2: ")

full_words = word_1 + word_2

length_1 = len(word_1)
length_2 = len(word_2)
length_3 = len(full_words)

length_1_float = float(length_1)
length_2_float = float(length_2)
length_3_float = float(length_3)

word_1_str = str(word_1)
word_2_str = str(word_2)
full_words_str = str(full_words)

is_on_in_both_words = "on" in full_words.lower()
is_ing_in_both_words = "ing" in full_words.lower()

sentence = "I hope this course is not full of jargon."
has_jargon = "jargon" in sentence

false_statement = "Mala" in "Maziwa"  

starts_same_letter = word_1[0].lower() == word_2[0].lower()

display = (f'''/n
===================== String Intelligence Analyzer ==========================  

Word 1: {word_1}
Word 2: {word_2}
Full Words: {full_words}

Length 1 (float): {length_1_float}
Length 2 (float): {length_2_float}
Length Total (float): {length_3_float}

Is "on" in Both Words: {is_on_in_both_words}
Is "ing" in Both Words: {is_ing_in_both_words}

Length Word 1: {length_1}
Length Word 2: {length_2}
Length Combined: {length_3}

Contains "jargon": {has_jargon}
False Statement Example ("Mala" in "Maziwa"): {false_statement}
Start With Same Letter: {starts_same_letter}
''')

print(f"{display}")
