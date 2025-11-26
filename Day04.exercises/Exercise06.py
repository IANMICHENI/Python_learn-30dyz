'''
Exercise 6 — Escape Sequences & Multi-line Strings

Goal: Practice \n, \t, triple quotes, and clean multi-line formatting.

Instructions (Plain Words):

Create a multi-line string that contains the following:

Name      Age     Country   City
Asabeneh  250     Finland   Helsinki


Use \t to align the columns.

Create another multi-line string using triple quotes, containing 2–3 sentences about yourself.

Include a backslash \ and double quotes " somewhere in your text.

Print both strings neatly.
'''
#Day 4 Of Learning Python
info = """Name      Age     Country   City
Asabeneh  250     Finland   Helsinki"""

print(f"\t {info}")

info_2 = """
Hello am\ Ian
Am learning Python
I enjoy\\ coding
"""
print(f"\n{info_2}")

