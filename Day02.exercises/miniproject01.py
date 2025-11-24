#Mini-project: Create a program that calculates and displays the user's BMI
user = input("Enter your name:")
weight = int(input("Enter your weight in Kg:"))
height = float(input("Enter your height in Meters: "))

bmi = weight / (height **2)

print(f"\n ===== BMI ===== ")
print(f"\n {user} , your BMI is {bmi:2f}")

#Add a category:Under,Over,Normal, Obese
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal weight")
elif 25 <= bmi < 30:
    print("Overweight")
else:
    print("Obese")