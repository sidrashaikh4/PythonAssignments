def person(name, surname="India"):
    print("Name",name ,"surname",surname)

n=input("Enter name")


m=input("Enter surname")

if m =="":
    person(n)
else:
    person(n,m)
