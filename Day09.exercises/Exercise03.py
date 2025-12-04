'''
Personal Workout Tracker

Objective:
Track your daily workouts, view progress, and calculate total calories burned.

Features:

Add a new workout:

Workout name (e.g., Running, Push-ups)

Duration in minutes

Calories burned per minute

View all workouts:

Show each workout with duration and calories burned

View total calories burned for the day

Delete a workout

Exit the program

Example Menu:

----------- Workout Tracker ------------
1. Add a New Workout
2. View all Workouts
3. View Total Calories Burned
4. Delete a Workout
5. Exit
Enter Choice (1 - 5):
'''
#Day 09 Of Learning Python
workouts = {}

while True:
    print("\n----------- Workout Tracker ------------")
    print("1. Add a New Workout")
    print("2. View all Workouts")
    print("3. View Total Calories Burned")
    print("4. Delete a Workout")
    print("5. Exit")
    
    choice = input("Enter Choice (1 - 5): ")
    
    if choice == "5":
        print("GoodBye!")
        break
    
    elif choice == "1":
        workout = input("Enter Workout Name: ").strip().title()
        if workout in workouts:
            print("Workout Already Exists")
        else:
            workouts[workout] = 0
            print("Workout '{workouts}' added")
            
    elif choice == "2":
        if not workouts:
            print("No Workouts Recorded")
        else:
            print("\n All WorkOuts:")
            for workout, items in workouts.items():
                print(f"{workouts}")
    elif choice == "3":
        if not workouts:
            print("No WorkOuts Recorded")
        else:
           duration = int(input("Enter duration"))
           cal_min = float(input("Enter calories burned per minute: "))
           
           