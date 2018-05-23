from random import randint
import random
print("get ready for cows and bulls game")
#cow and bull games:)
number=int(input("enter a four digit number"))
i=randint(1000,9999)
number = str(number)
print(i)
cow=0
buffalos=0
i= str(i)
for j in range (0,4):
    if number[j] ==i[j]:
        cow = cow+1

print(number)
print("cows are" ,cow,"buffalos are", 4-cow)