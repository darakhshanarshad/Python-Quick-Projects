#number checker:
#1 ask user for any number.
#2 check is it even or odd number.

no = int(input("enter a number: "))
if no  %2 == 0:
     print(no," is an even number.")

else:
    print(no, "is an odd number")


#positive , negative or zero:
num = int(input("enter number: "))
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("zero")

#largest number of two numbers:
l = int(input("enter 1st number:"))
print(l)
m = int(input("enter 2nd number:"))
print(m)

if l < m:
    print(m, "is largest number")

else:
    print(l," is largest number")


