#.Program to print the greatest number in given three numbers?
num1=int(input())
num2=int(input())
num3=int(input())
if num1>num2 and num1>num3:
    print("num1 is greatest number")
elif num2>num3 and num2>num1:
    print("num2 is greatest number")
else:
    print("num3 is greatest")
      