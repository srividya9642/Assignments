#Program to calculate the sum of the first 10 natural numbers using for Loop- for loop and while loop?
n=10
sum=0
'''for i in range(1,n+1):
    sum+=1
    print(sum)'''
#sum using while loop
i=1
while i<=n:
    sum+=i
    i+=1

print(sum)