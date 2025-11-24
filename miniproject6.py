#Tiny Banner: Ask the user for their name and print it as a mini ASCII banner using repeated symbols (*, #, etc.).
name = input("Enter you Name: ")


print(f"*" * (len(name)+5))
print(f"* {name} *")
print(f"*" * (len(name)+5))


print(f"=" * (len(name)+5))
print(f"# {name} #")
print(f"=" * (len(name)+5))