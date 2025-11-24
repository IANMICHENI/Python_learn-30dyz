#Ask the user for two numbers and swap them without using a third variable.
num_1 = float(input("Enter first Number: "))
num_2 = float(input("Enter Second: "))

num_1 = num_1 + num_2  
num_2 = num_1 - num_2  
num_1 = num_1 - num_2 

print(f"After swapping num_1 = {num_1}, num_2 = {num_2}")
