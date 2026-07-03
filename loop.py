#Multiplication table:

no = int(input("enter the number:"))
for t in range(1 , 11):
    print(no,"x" , t ,"=" ,t *no )


#sum of 1 to 10 numbers:
total = 0
for i in range(1 ,10):
    total = total + i
    print(total)

#count sum of even numbers (1 to 50):
total = 0
for i in range(1 , 51):
    if  i %2 == 0:
        total = total + i
        print(total)

#count even numbers from 1 to 50:
for m in range (1, 51):
    if m %2 == 0:
        print(m)


#count odd numbers:
for o in range(1, 51):
    if o %2 != 0:
        print(o)



#marks calculator:
marks = int(input("enter your marks:"))
if marks >= 80:
    print("grade A")
elif marks >= 70:
    print("grade B")
elif marks >= 60:
    print("grade C")
else:
    print("fail")