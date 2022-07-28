fruits=['Banana','Mango','cherry','orange','Apple']
print(fruits)
t=(input("enter fruit name to remove:"))
if t in fruits:

    fruits.remove(t)
    print(fruits)
else:
    print ("Not Found")
