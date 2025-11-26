''' 
Project 4 — Text Adventure Analyzer

Goal: Build a small “text adventure” analyzer that examines user inputs and gives fun statistics and modifications.

Instructions:

Ask the user for inputs:

Character name

Favorite weapon

Favorite spell

Adventure location (city/forest/dungeon)

String Operations:

Print a multi-line introduction for the adventure using \n and \t.

Count the total number of characters in each input.

Convert the name to:

Uppercase

Lowercase

Title case

Swapcase

Check if the name contains any spaces (using in).

Slice the first 3 letters of the weapon and the last 3 letters of the spell.

Replace spaces in the location with underscores.

Search & Indexing:

Find the first character of the name.

Find the index of the letter 'a' in the weapon (if present).

Check if the spell starts with 'Fire' and ends with 'Blast'.

List & Join:

Create a list of all inputs [name, weapon, spell, location].

Join the list into a single string separated by ' -> '.

Print a Summary:

Use f-strings and a multi-line string to show:

Original inputs

Modified strings

Slice results

Search results

Joined list
'''
#Day 04 of Learning Python

character_name = input("Enter Character Name: ")
favorite_weapon = input("Enter your Favourite Weapon: ")
favorite_spell = input("Enter Favorite Spell: ")
adventure_location = input("Enter Adventure Location (city/forest/dungeon): ")

char_len = len(character_name)
weapon_len = len(favorite_weapon)
spell_len = len(favorite_spell)
location_len = len(adventure_location)

upper_name = character_name.upper()
lower_name = character_name.lower()
title_name = character_name.title()
swap_name = character_name.swapcase()
has_space = " " in character_name

slice_weapon = favorite_weapon[0:3]
slice_spell = favorite_spell[-3:]
location_modified = adventure_location.replace(" ", "_")

first_char = character_name[0]
index_a = favorite_weapon.find("a") 
starts_fire = favorite_spell.startswith("Fire")
ends_blast = favorite_spell.endswith("Blast")

inputs_list = [character_name, favorite_weapon, favorite_spell, adventure_location]
joined_inputs = " -> ".join(inputs_list)

summary = f'''
============ TEXT ADVENTURE SUMMARY ============
Original Inputs:
Character Name: {character_name}
Favorite Weapon: {favorite_weapon}
Favorite Spell: {favorite_spell}
Adventure Location: {adventure_location}

Character Transformations:
Uppercase: {upper_name}
Lowercase: {lower_name}
Title Case: {title_name}
Swapcase: {swap_name}
Contains space: {has_space}
First character: {first_char}

Sliced Inputs:
Weapon first 3 letters: {slice_weapon}
Spell last 3 letters: {slice_spell}
Location with underscores: {location_modified}

Search Results:
Index of 'a' in weapon: {index_a}
Spell starts with 'Fire': {starts_fire}
Spell ends with 'Blast': {ends_blast}

Joined Inputs: {joined_inputs}
==============================================
'''
print(summary)
