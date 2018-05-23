a=int(input("enter the number to check divisor"))
#add the divisor to list and print
list=[]
for i in range (1,a):
    if a%i == 0:
        list.append(int(i))
print(list)