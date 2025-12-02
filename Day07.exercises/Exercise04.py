''' 
Online Store Cart

Objective: Manage a shopping cart for an online store.

Features:

Store items as key with quantity or price: {'apple': {'price': 2, 'quantity': 3}}

Add items to cart.

Remove items.

Update quantity.

Calculate total price.

List items and details neatly.
'''
fruits = {
    'apple': {'price': 2, 'quantity': 3},
    'Oranges': {'price': 3, 'quantity': 4},
    'Mangoes': {'price': 5, 'quantity': 2}
}

fruits['Kiwi'] = {'price': 4, 'quantity': 6}
print(fruits)

fruits.pop('Oranges')
print("\n", fruits)

fruits['Mangoes']['quantity'] = 10
print("\n", fruits)

total_price = 0

for fruit, info in fruits.items():
    total_price += info['price'] * info['quantity']

print(f"\n Total_price:{total_price}")