print("   Email Validator   ")  #check whether an email follows a basic valid pattern.

email = input("Enter your Email: ")

for i in range(1):

    if email != "":

        if "@" in email :
            email += email
            # print("good")
        else:
            print(f"( @ ) is required." )

        if "gmail" in email:
            email += email
            # print("nice")
        else:
            print("(gmail) is required!")

        if ".com" in email:
            email += email
            # print("great")
        else:
           print("(.com) is required ! ")

        if "@gmail.com" in email:
            print("verifying")
        else:
            print("@gmail.com is must in the end of gmail!")
    else:
        print("email must not empty!")