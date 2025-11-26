'''
Project 2 — String Analyzer & Manipulator

Goal: Deep dive into string methods, indexing, slicing, and searching.

Instructions:

Ask the user for a sentence.

Perform the following:

Print the first, last, and middle character

Count the number of times 'a' appears

Check if it starts with "Python" and ends with "challenge"

Replace "Python" with "Java"

Convert it to upper, lower, title, and swapcase

Slice out the first 10 characters

Slice out the last 10 characters

Reverse the sentence

Split the sentence into words

Print length of sentence and number of words

Print a formatted multi-line summary of all results
'''
#Day 04 of Learning Python
sentence = "Python makes coding a fun challenge"

first_char = sentence[0]
last_char = sentence[-1]
middle_char = sentence[len(sentence) // 2]

count_a = sentence.lower().count('a')

starts_python = sentence.startswith("Python")
ends_challenge = sentence.endswith("challenge")

replaced = sentence.replace("Python", "Java")

upper_case = sentence.upper()
lower_case = sentence.lower()
title_case = sentence.title()
swap_case = sentence.swapcase()

first_10 = sentence[:10]
last_10 = sentence[-10:]

reversed_sentence = sentence[::-1]

words = sentence.split()
num_words = len(words)

length = len(sentence)

summary = f"""
========== SENTENCE ANALYSIS SUMMARY ==========

Original Sentence:
{sentence}

Characters:
  First: {first_char}
  Middle: {middle_char}
  Last: {last_char}

Counts:
  'a' appears {count_a} times

Checks:
  Starts with "Python": {starts_python}
  Ends with "challenge": {ends_challenge}

Replaced:
  {replaced}

Case Formats:
  Uppercase: {upper_case}
  Lowercase: {lower_case}
  Title: {title_case}
  Swapcase: {swap_case}

Slices:
  First 10 chars: {first_10}
  Last 10 chars: {last_10}

Reverse:
  {reversed_sentence}

Word Info:
  Words: {words}
  Number of words: {num_words}
  Sentence length: {length} characters

---------------------------------------
"""

print(summary)
