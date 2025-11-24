#Build a simple Card program that prints a formatted Bio
#Bio of Me: Name,Age,Country, School

name = input("Enter Your Name:")
age = int(input("Enter Your Age:"))
country = input("Enter your Country:")
school_name = input("Enter your School Name:")

intro_card = (f"""
==========================
         ABOUT ME        
==========================
    Hello!
My name is {name}
I am {age} years old
I live in {country}
I study at {school_name}

Nice to meet you {name}
""")

print(f"{intro_card}")
