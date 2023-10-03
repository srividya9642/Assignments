#.Program to print min numbers in given 3 numbers?
a=input("enter a value")
b=input("enter b value")
c=input("enter c value")
min=0
if a<b and a<c:
    min=a
elif b<c:
    min=b
else:
    min=c
    print(min,"is the min of three numbers")