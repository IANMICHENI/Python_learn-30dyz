#Star Pattern Creator: Ask the user for a number and print a triangle/star pattern that many lines tall.

pattern = int(input(" Enter Number: "))

for i in range(1 , pattern + 1):
    print("*" * i)