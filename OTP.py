print("    OTP Generator & Verifier    ") 

import random 
import string

generate = ""

for i in range(6):
    
    my_otp =  random.choice(string.digits)
    generate +=  my_otp
print(generate)
    

otp = (input("Enter your OTP: "))


if otp == generate:
    print("verify")
    

else:
    print("Enter correct OTP!")