n=int(input("enter size of list"))
list=[]
print("enter the elements of list")
for i in range (0,n):
    c=int(input(""))
    list.append(c)
print("the list is ")
print(list)
flag = 0
search=int(input("enter the number you want to search in list"))
#mid= (l+1)/
for j in range(0,n):
    if list[j] == search:
        print("found at pos",j+1)
        break
    else:
        print("element not found")
        break
