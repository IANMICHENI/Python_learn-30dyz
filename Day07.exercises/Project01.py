''' 
Personal Library Management System

Objective: Manage books with details like author, genre, and availability using dictionaries and sets.

Features:

Store books as dictionaries with title as key and nested dictionary for details (author, genre, available).

Add new books.

Remove books.

Update availability status.

Count books per genre.

List all unique authors (use a set).

Sort books alphabetically by title.

Find books by a particular genre or author.
'''
#Day 07 of Learning Python
library = {
    '1984': {'author': 'George Orwell', 'genre': 'Dystopian', 'available': True},
    'Harry Potter': {'author': 'J.K. Rowling', 'genre': 'Fantasy', 'available': False},
    'The Hobbit': {'author': 'J.R.R. Tolkien', 'genre': 'Fantasy', 'available': True}
}

library['Alfakher'] = {'author': 'Zendiambo', 'genre': 'Sherahh', 'available': True}

print(f"\n----------- Added ------------")
print(library)

print(f"\n----------- Remove ------------")
library.pop('1984')
print(library)

print(f"\n----------- Update ------------")
library['Harry Potter']['available'] = True
print(library)

print(f"\n----------- Count ------------")
genre_count = {}
for book, info in library.items():
    genre_count[info['genre']] = genre_count.get(info['genre'], 0) + 1
print(genre_count)

print(f"\n----------- Unique Authors ------------")
authors = {info['author'] for info in library.values()}
print(authors)

print(f"\n----------- Sorted Authors ------------")
sorted_books = sorted(library.keys())
print(sorted_books)
