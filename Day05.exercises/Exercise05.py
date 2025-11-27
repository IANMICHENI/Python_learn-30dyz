'''
EXERCISE 5 — Grocery List Management System

Start with:

groceries = ["milk", "bread", "eggs", "butter", "bananas", "apples"]

Tasks:

Print:

length

first, middle, last items

Modify:

change "eggs" → "organic eggs"

Add:

append "yogurt"

insert "watermelon" at index 2

Remove:

pop last item

remove "bread"

Slice:

items 2 to 5

reverse slice (backwards slicing)

Reverse the list

Sort alphabetically

Join all items with " | "

Copy list into backup_list
'''
#Day 05 of Learning Python

print("\n ========== Grocery List Management System ==========")
groceries = ["milk", "bread", "eggs", "butter", "bananas", "apples"]


print("--------------- LENGTH --------------")
groc_length = len(groceries)
print(groc_length)

first_item = groceries[0]
last_item = groceries[-1]
middle_item = groceries[3]

print(first_item )
print(last_item )
print(middle_item)

print("--------------- Modify --------------")
index = groceries.index("eggs")
groceries[index] ="Organic Eggs"
print(groceries)

print("--------------- ADD -----------------")
groceries.append("Yorgut")
print(groceries)
groceries.insert(2,"Watermelon")
print(groceries)

print("--------------- Remove -----------------")
groceries.pop(-1)
groceries.remove("bread")
print(groceries)

print("--------------- SLICE -----------------")
groc_slice = groceries[2:5]
groc2_slice = groceries[::-1]

print(groc_slice)
print(groc2_slice)

print("\n------------ SORT -------------")
groceries.sort()
print(groceries)
groceries.sort(reverse=True)
print(groceries)

print("\n------------ COPY -------------")
backup_list = groceries.copy()
print(backup_list)

print("\n------------ JOIN -------------")
groceries = " | ".join(groceries)
print(groceries)