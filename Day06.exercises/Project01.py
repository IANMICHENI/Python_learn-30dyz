'''
Book Collection Manager

Objective: Manage a personal book collection with genres and authors using tuples and sets.

Features:

Store books as tuples: (title, author, genre)

Convert tuples into sets to remove duplicate books.

Add new books using add() or update()

Remove books you no longer own.

Find books by a specific author (filter using set intersection).

List all genres (unique) using a set.

Count how many books you have per genre.

Sort the final list of books alphabetically by title.
'''
# Day 06: Book Collection Manager

# Step 1: Store books as tuples
book1 = ('1984', 'George Orwell', 'Dystopian')
book2 = ('Harry Potter', 'J.K. Rowling', 'Fantasy')
book3 = ('The Hobbit', 'J.R.R. Tolkien', 'Fantasy')
book4 = ('1984', 'George Orwell', 'Dystopian')  

books_set = {book1, book2, book3, book4}
print(books_set)

books_set.add(('Brave New World', 'Aldous Huxley', 'Dystopian'))
books_set.update([
    ('Moby Dick', 'Herman Melville', 'Classic'),
    ('Pride and Prejudice', 'Jane Austen', 'Classic')
])

books_set.discard(('1984', 'George Orwell', 'Dystopian'))

fantasy_books = {b for b in books_set if b[2] == 'Fantasy'}
print(fantasy_books)

genres = {b[2] for b in books_set}
print(genres)

genre_count = {genre: sum(1 for b in books_set if b[2] == genre) for genre in genres}
print(genre_count)

sorted_books = sorted(books_set, key=lambda x: x[0])
print(sorted_books)
