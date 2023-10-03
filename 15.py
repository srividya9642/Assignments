#Program to print max numbers in given 3 numbers?
a=input("enter a value")
b=input("enter b value")
c=input("enter c value")
max=0
if a>b and a>c:
    max=a
elif b>c:
   max=b
else:
    max=c
    print(max,"is the max of three numbers")