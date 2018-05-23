number=int(input("enter the no to check prime or not"))
n=int(number/2)
flag=0
for i in range(2,n+1):
        if number % 2 == 0:
            flag = 1
if flag == 1:
    print("not a prime number")
else:
    print('prime number')
