#Ask the user for their age in years, then calculate and print their age in months, days, and hours.
age = int(input("Enter age in years: "))

months = age * 12
days = age * 365
hours = days * 24

print(f"You are {months} months old, {days} days old, and {hours} hours old.")