'''  
EXERCISE 3 — Country Analyzer

Start with this list:

countries = ['Kenya', 'Uganda', 'Tanzania', 'Ethiopia', 'Rwanda', 'Burundi', 'Somalia']

Tasks:

Unpack:

ke, ug, tz, *others = countries


Slice:

first 3

last 3

middle countries

Check membership:

is "Kenya" in the list?

is "Egypt" in the list?

Modify:

change "Somalia" to "Somaliland"

Insert "South Sudan" after Kenya

Remove Ethiopia

Clear the list

Destroy the list using del
'''
#Day 05 of learning Python

countries = ['Kenya', 'Uganda', 'Tanzania', 'Ethiopia', 'Rwanda', 'Burundi', 'Somalia']
ke, ug, tz, *others = countries

print(ke)
print(ug)
print(tz)
print(others)

print("------------ SLICE ------------")
print(countries[0:3])
print(countries[4:7])
print(countries[3:4])

print("------------ CHECK MEMBERSHIP ------------")
is_kenya = "Kenya" in countries
print(is_kenya)
is_egypt = "Egypt" in countries
print(is_egypt)

print("------------ MODIFY ------------")
index = countries.index("Somalia")
countries[index] = "Somaliland"
print(countries)

print("------------ INSERT ------------")
countries.insert(1,"SouthSudan")
print(countries)

print("------------ DELETE ------------")
countries.pop(5)
print(countries)

print("------------ CLEAR LIST ------------")
countries.clear()
print(countries)

print("------------ DEL ------------")
del countries


