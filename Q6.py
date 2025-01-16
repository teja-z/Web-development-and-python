a=int(input("Enter the number " ))
sum=0
temp=a 
while temp>0:
    r=temp%10
    temp=temp//10
    sum=sum*10+r 
print("Reverse of the number is",sum)
