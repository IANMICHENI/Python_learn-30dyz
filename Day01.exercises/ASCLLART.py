#Write A Script that prints a multi-line ASCLL art (Pattern)
print("""
        *
       ***
      *****
    ********
   **********
  ************
 **************
   ***********
    *********
     *******
      *****
       ***
        *
    """)

#Simple ASCII art name card#

name = "Ian"
print("*" * (len(name)+5))
print(f"* {name} *")
print("*" * (len(name)+5))