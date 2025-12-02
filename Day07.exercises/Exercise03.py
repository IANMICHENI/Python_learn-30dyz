''' 
Library Book Inventory

Objective: Manage books in a library using dictionaries.

Features:

Book title as key, details as a dictionary: {'1984': {'author':'Orwell','genre':'Dystopian'}}

Add new books.

Remove books.

Search books by author or genre.

Count how many books per genre.

List all books sorted alphabetically.
'''
#Day 07 of Learning Python
library = {'1984': {'author':'Orwell','genre':'Dystopian'}}
library['Kilio'] = {'author':'Peter','genre':'Hadithi'}
library['Machozi'] = {'author':'James','genre':'Thriller'}
library['Cry'] = {'author':'John','genre':'Action'}
library['Tears'] = {'author':'Luke','genre':'Fantasy'}

print(library)
library.pop('Kilio')
print(library)

print('Kilio' in library)
print('1984' in library)

count = {}

for title, info in library.items():
    genre = info['genre']
    count[genre] = count.get(genre,0)+1
    print(count)
    
sorted_books = sorted(library, key=lambda library: library[0])

print("\nSorted books:")
for b in sorted_books:
    print(b)