r=int(input("enter the terms of fibnocci series"))
a=1
b=1
print(a)
print(b)
c = 0
for i in range(0,r):
    c = int(a + b)
    print(c)

    a=b
    b=c
