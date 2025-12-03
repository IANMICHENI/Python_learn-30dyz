'''
Daily Expense Tracker

Objective: Track your daily expenses and get a summary.

Features:

Add a new expense (name, amount, category).

View all expenses.

View total spent per category.

View overall total spending.

Exit the program.
'''
# Day 09 Of Learning Python

# Daily Expense Tracker
expenses = {}

while True:
    print("\n----------- Daily Expenses ------------")
    print("1. Add a New Expense")
    print("2. View all Expenses")
    print("3. View total spent per category")
    print("4. View overall total spending")
    print("5. Exit")
    
    choice = input("Enter Choice (1 - 5): ").strip()
    
    if choice == "5":
        print("GoodBye")
        break
    
    elif choice == "1":
        name = input("Enter expense name: ").strip().title()
        category = input("Enter expense category: ").strip().title()
        amount = float(input("Enter expense amount: "))
        
        if category not in expenses:
            expenses[category] = []
        expenses[category].append({"name": name, "amount": amount})
        print(f"Expense '{name}' of ${amount:.2f} added under '{category}' category.")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded yet.")
        else:
            print("\nAll Expenses:")
            for category, items in expenses.items():
                print(f"\nCategory: {category}")
                for item in items:
                    print(f"  - {item['name']}: ${item['amount']:.2f}")

    elif choice == "3":
        if not expenses:
            print("No expenses recorded yet.")
        else:
            print("\nTotal Spent Per Category:")
            for category, items in expenses.items():
                total = sum(item['amount'] for item in items)
                print(f"  {category}: ${total:.2f}")

    elif choice == "4":
        if not expenses:
            print("No expenses recorded yet.")
        else:
            total_spent = sum(
                item['amount'] for items in expenses.values() for item in items
            )
            print(f"\nOverall Total Spending: ${total_spent:.2f}")

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
