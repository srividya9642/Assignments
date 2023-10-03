#Program to check if a number is a 3-digit number or not
num=int(input())
print(type(num))
num=str(num)
if len(num)==3:
      print("The number entered has 3 digits.")
else: 
      print("The number entered isn't of 3 digits.")