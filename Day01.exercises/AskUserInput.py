#Script that asks user for their name, and greets them using a personalized message
name = input("Enter Your Name: ")
print(f"Hello {name}, How are you?") 

#Repeat user’s name multiple times#
times = int(input("Enter times to repeate Name: "))
print((name + "\n" ) * times)