#Print min numbers in given 3 numbers - using Ternary Operator?
a=input("enter a value")
b=input("enter b value")
c=input("enter c value")
print(a) if (a<b and a<c) else (print(b) if b<c else print(c))
