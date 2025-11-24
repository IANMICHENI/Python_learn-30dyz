#Multiline message using """ and print it

message = """
    1. Print your name, age, and favorite hobby.
    2. Write a script that prints “Python is awesome!” 10 times.
    3. Ask a user for their name and greet them.
    4. Create a multiline message using and print it.
    5. Mini-project: Build a simple “Introduction Card” program that prints a formatted bio. 
"""
print(f"{message}") 

#Ask the user for their name and favorite hobby, then print a multi-line message.
name = input("Enter your Name:")
hobby = input("Enter your favourite Hobby:") 

mango = (f"""
      Your name is {name}
      Your Favourite hobby is {hobby}
    """)
print(f"{mango}")
