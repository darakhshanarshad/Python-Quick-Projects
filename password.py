print("  Password  ")
print("-" * 20)
import time

pass_word = "2468"

for user_password in range(3):
    user_password = (input("Enter Password: "))
    if user_password == pass_word:
        print("Correct Password , Access Granted")
        print('_' * 10)
        break
    else:
        print("Retry!")
        
else:
    print("locked for 10sec")

    for second in range(10 , 0 , -1):
        print(f"Countdown: {second}")
        time.sleep(1)
    print("Try Again")

    
        

