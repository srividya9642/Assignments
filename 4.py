#Program to check if a number is multiple of 3 not not?
num=int(input())
sum=0
while num!=0:
    temp=num%10
    sum=sum+temp
    num=num//10
if sum%3==0:
    print("multiple of 3")
else:
    print("not a multiple of 3")