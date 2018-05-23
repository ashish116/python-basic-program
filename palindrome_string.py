string=input("enter the string to check palindrome")
#[::-1] is used to reverse a string
rv=string[::-1]
print(rv)
if string == rv:
    print("palindrome")
else:
    print("not palindrome")