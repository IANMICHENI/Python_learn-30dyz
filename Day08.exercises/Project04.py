'''
Movie Recommendation & Age Restriction System
Objective:

Ask the user about their age and favorite movie genres.
Recommend movies based on their taste AND ensure they are old enough for the age rating.

Features:
Input:

Ask the user for their age

Ask the user to input favorite genres separated by commas
(e.g., "Action, Horror, Drama")

Movie Database (with age limits):
movies = {
    "action": {"Mad Max", "John Wick", "Mission Impossible"},
    "comedy": {"Home Alone", "The Mask", "Superbad"},
    "horror": {"The Conjuring", "It", "A Quiet Place"},
    "drama": {"Shawshank Redemption", "Forrest Gump", "The Godfather"},
    "sci-fi": {"Interstellar", "Inception", "The Matrix"}
}

age_limits = {
    "action": 16,
    "comedy": 10,
    "horror": 18,
    "drama": 13,
    "sci-fi": 13
}
'''
# Day 08 Of Learning Python

movies = {
    "action": {"Mad Max", "John Wick", "Mission Impossible"},
    "comedy": {"Home Alone", "The Mask", "Superbad"},
    "horror": {"The Conjuring", "It", "A Quiet Place"},
    "drama": {"Shawshank Redemption", "Forrest Gump", "The Godfather"},
    "sci-fi": {"Interstellar", "Inception", "The Matrix"}
}

age_limits = {
    "action": 16,
    "comedy": 10,
    "horror": 18,
    "drama": 13,
    "sci-fi": 13
}
age = int(input("Enter Your Age: "))

genres_input = input("Enter Favourite Genres (comma separated): ")

genres = [g.strip().lower() for g in genres_input.split(",")]

valid_found = True

print("\n--- Movie Recommendations ---")

for genre in genres:
    if genre in movies:
        valid_found = False
        required_age = age_limits[genre]

        if age >= required_age:
            print(f"\nSince you like {genre.title()}, you can watch:")
            for m in movies[genre]:
                print(f" - {m}")
        else:
            print(f"\n You are too young for {genre.title()} movies. Minimum age: {required_age}.")

if not valid_found:
    print("Unknown genres. Please enter valid genres like Action, Horror, Drama, etc.")
