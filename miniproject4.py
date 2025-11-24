#Simple Quote Printer: Let the user enter their favorite quote and author, then print it in a styled multi-line format.
quote = input("Enter your Favourite Quote: ")
author = input("Enter Authors name: ")

print(f"""  
    ==========
    {quote}
    by:{author}
    ==========
    """)