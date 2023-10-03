#Program to print given 3 numbers in ascending order?
#num=int(input())
#numbers=[1,4,3,2]

#print(numbers.sort())
#print(numbers)

num1,num2,num3=input("enter three values").split()
if num1<num2 and num1<num3:
    if num2<num3:
     x,y,z=num1,num2,num3
    else:
       x,y,z=num1,num2,num3
elif num2<num3 and num2<num1:
   if num3<num1:
      x,y,z=num1,num2,num3
   else:
      x,y,z=num1,num2,num3
else:
   if num1<num2:
    x,y,z=num1,num2,num3
   else:
      x,y,z=num1,num2,num3
      print(x,y,z)
        

