'''  
Project 3 — Company & Library Text Analyzer

Goal: Combine everything: concatenation, slicing, searching, string methods, and formatting.

Instructions:

Create variables for:

company = "Coding For All"

libraries = "Django, Flask, NumPy, Matplotlib, Pandas"

Perform operations on company:

Find first, last, and 10th character

Slice out "Coding"

Check if "Coding" exists (in)

Replace "Coding" with "Python"

Check if it starts with "Coding" and ends with "All"

Split into words

Perform operations on libraries:

Split into a list using ,

Join the list with #

Count occurrences of 'a'

Check if 'Flask' is in the list

Print a formatted summary using f-strings and multi-line strings that shows:

Original texts

Modifications

Results of searches, slices, and replacements
'''
#Day 04 of Learning Python

company = "Coding For All"
libraries = "Django, Flask, NumPy, Matplotlib, Pandas"

first_char = company[0]
last_char = company[-1]
length_char = company[9]

slicing_coding = company[0:6] 

checkin = "Coding" in company

print(company.replace("Coding","Python")) 

start_Codin = company.startswith("Coding")

end_all = company.endswith("All")

print(company.split()) 

library_list = libraries.split(", ")
joined_library = " # ".join(library_list)
libraries_occur = libraries.count("a")
is_flask_present = "Flask" in libraries

analyzer = (f'''
============ Company & Library Text Analyzer ============

                    Original Text
---------------------------------------------------------
Company:{company}
Libraries:{libraries}
---------------------------------------------------------
                    Modifications
First Character:{first_char}
Last Character:{last_char} 
10th Character:{length_char}

Slicing Coding:{slicing_coding}
Checkin:{checkin}  
 
Starts with Coding:{start_Codin}
Ends with All:{end_all}

Library list:{library_list}
Joined Library:{joined_library}
Libraries Occurance:{libraries_occur}

Is Flask Present:{is_flask_present}            
----------------------------------------------------------
''' )
print(analyzer)