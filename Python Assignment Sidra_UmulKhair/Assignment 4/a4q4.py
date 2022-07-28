n=int(input("Enter a number"))
temp=n
rev=0
while (n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("Number is PALINDROMe")
else:
    print("Not Palindrome")

string=input("Enter A string")
if(string==string[::-1]):
    print("string is PALINDROMe")
else:
    print("Not Palindrome")