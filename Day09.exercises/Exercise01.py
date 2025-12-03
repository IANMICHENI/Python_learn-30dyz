'''
Create a Python program that allows users to:

Add new habits they want to track

Mark habits as completed for the day

View all habits

View progress summary

Exit the program
'''
# Day 09 Of Learning Python - Habit Tracker

habits = {}  # Store habits and progress

while True:
    print("\nHabit Tracker Menu: ")
    print("1. Add a New Habit")
    print("2. Mark Habit as Completed")
    print("3. View all Habits")
    print("4. View Progress Summary")
    print("5. Exit")
    
    choice = input("Enter your Choice (1 - 5): ").strip()

    if choice == "1":
        habit = input("Enter the New Habit Name: ").strip().title()
        if habit in habits:
            print("Habit Already Exists")
        else:
            habits[habit] = 0
            print(f"Habit '{habit}' added.")
            
    elif choice == "2":
        habit = input("Which habit did you complete today? ").strip().title()
        if habit in habits:
            habits[habit] += 1
            print(f"Great! You completed '{habit}' today.")
        else:
            print("Habit not found!")
            
    elif choice == "3":
        if not habits:
            print("No habits added yet.")
        else:
            print("\nYour Habits:")
            for h, count in habits.items():
                print(f"- {h}: {count} days completed")
                
    elif choice == "4":
        if not habits:
            print("No habits to summarize.")
        else:
            total_habits = len(habits)
            total_completions = sum(habits.values())
            print(f"\nYou have {total_habits} habit(s) tracked.")
            print(f"Total completions so far: {total_completions}")
            print("Detailed progress:")
            for h, count in habits.items():
                print(f"- {h}: {count} days completed")
                
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please select 1-5.")
