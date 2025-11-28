'''
Unique Words Analyzer

Objective: Use tuples and sets to find unique words.

Tasks:

Take a sentence:

sentence = "I am a teacher and I love to inspire and teach people"


Split the sentence into words (list).

Convert the list to a set to find unique words.

Count how many unique words there are.

Convert back to a tuple and slice the first half and second half.

Print all unique words sorted alphabetically.
'''
#Day 06 Of Learning Python

sentence = "I am a teacher and I love to inspire and teach people"

sen_list = sentence.split()
print(sen_list)

unique_words_set = set(sen_list)
print(unique_words_set)

unique_count = len(unique_words_set)
print(unique_count)

unique_words_tuple = tuple(unique_words_set)
print(unique_words_tuple)

mid_index = len(unique_words_tuple) // 2
first_half = unique_words_tuple[:mid_index]
second_half = unique_words_tuple[mid_index:]

print("First half:", first_half)
print("Second half:", second_half)

sorted_words = sorted(unique_words_tuple)
print("Sorted unique words:", sorted_words)
