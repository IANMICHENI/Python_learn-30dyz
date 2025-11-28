'''
Grocery Inventory Tracker

Objective: Manage grocery inventory using sets and tuples.

Tasks:

Start with a tuple of groceries: groceries = ('milk', 'bread', 'eggs', 'butter', 'apples', 'milk')

Convert it to a set to remove duplicates.

Add new items to the set using add() and update().

Remove expired items using discard().

Create another set for vegetables = {'onion', 'carrot', 'apples'}.

Find and print:

All items (union)

Items common in both (intersection)

Items only in groceries (difference)

Items in either but not both (symmetric difference)

Convert the set back to a tuple and print the sorted grocery list.
'''
#Day 06 of Learning Python
groceries = ('milk', 'bread', 'eggs', 'butter', 'apples', 'milk')

vegetables = ('onion', 'carrot', 'apples')

set_1 = set(groceries)
set_1.add("Maziwaa")
set_1.update(["Oranges","grapes"])

set_1.discard("Maziwaa")

set_2 = set(vegetables)


union_result = set_1.union(set_2)
print(union_result)

inter = set_1.intersection(set_2)
print(inter)

diff = set_1.difference(set_2)
print(diff)

sym_diff = set_1.symmetric_difference(set_2)
print(sym_diff)

tuple_a = tuple(set_1)
tuple_b = tuple(set_1)
print (tuple_a)
print(tuple_b)