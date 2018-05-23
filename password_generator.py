from random import randint
import string
import random
choice=input("do you want a strong password??\n yes or no")
string=""

if choice == "yes":
    for i in range (0,4):

        i=randint(0,9)
        string= string + str(i)
    for j in range (0,4):
        k=randint(65,120)
        string= string + chr(k)
print(string)

