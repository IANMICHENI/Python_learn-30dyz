''' 
Season Checker

Ask the user for a month (string) and print the season:

Autumn → September, October, November

Winter → December, January, February

Spring → March, April, May

Summer → June, July, August
'''
# Day 08 Of Learning Python
month = input("Enter MOnth: ")

if month in ("September, October, November"):
    print("Autumn")
elif month in ("December, January, February"):
    print("Winter")
elif month in ("March, April, May"):
    print("Spring")
elif month in ("June, July, August"):
    print("Summer")
else:
    print("No Season")
