print("   Username Generator    ") 
print("-" * 25)
import random

name = input("Enter Your Name Please: ").lower()

parts = name.split()                        #break name if last name exist.
name = "_".join(parts)                       #join them "_" with underscore.

number = random.randint(1 , 999)

user_name = name + str(number)

print(f"User_name suggestion: {user_name}" )