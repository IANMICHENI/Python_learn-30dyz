'''
Nordic Countries Checker

Objective: Work with tuples and sets to check countries.

Tasks:

Create a tuple of nordic countries:

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')


Check if 'Estonia' and 'Iceland' are nordic countries.

Convert the tuple to a set for additional operations.

Add 'Greenland' and 'Faroe Islands'.

Remove 'Denmark'.

Slice the tuple/set to get first 3 and last 3 countries.
'''
#Day 06 0f Learning Python

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

is_estonia_nordic = 'Estonia' in nordic_countries
print(is_estonia_nordic)
is_ice_land = 'Iceland' in nordic_countries
print(is_ice_land)

set_a = set(nordic_countries)
set_a.update(["Greenland","Faroe Islands"])

set_a.remove("Denmark")

set_aa = len(set_a)
print(set_aa)

nord_list = list(set_a)

first3 = nord_list[:3]
last3 = nord_list[-3:]

print(first3)
print(last3)