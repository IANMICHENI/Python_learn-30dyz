'''
Personal Contact Book

Objective: Manage a personal contact book using dictionaries.

Features:

Store contacts with name as key and details as nested dictionary:

contacts = {
    'Alice': {'phone': '0712345678', 'email': 'alice@email.com'}
}


Add new contacts.

Update phone/email.

Delete contacts.

Search for a contact.

List all contact names.
'''
#Day 06 Of Learning Python
contacts = {
    'Alice': {'phone': '0712345678', 'email': 'alice@email.com'}
}

contacts['Mwangi'] = {
    'phone': '0799887766',       
    'email': 'mwangi@email.com'  
}
print("After adding Mwangi:", contacts)

contacts['Alice']['phone'] = '07897979790'
print("After updating Alice phone:", contacts)

contacts.pop('Alice')
print("After deleting Alice:", contacts)

print("\nContact Names:")
for name in contacts.keys():
    print(name)

search_name = "Mwangi"
if search_name in contacts:
    print("\nContact found:", contacts[search_name])
else:
    print("\nContact not found!")
