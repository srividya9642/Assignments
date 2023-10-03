#Program to print given 3 numbers in descending order?
num1,num2,num3=input("enter three numbers").split()
if num1<num2 and num1<num3:
    x,y,x=num1,num2,num3
    if num2<num3:
        x,y,z=num1,num2,num3
    else:
        x,y,z=num1,num2,num3
elif num2<num3 and num2<num1:
    if num1<num3:
        x,y,z=num1,num2,num3
    else:
        x,y,z=num1,num2,num3
else:
    if num1<num2:
        x,y,z=num1,num2,num3
    else:
        x,y,z=num1,num2,num3
        print(x,y,z)




