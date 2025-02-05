n = int(input("Enter the number:"))
temp=n
def add_digit(num):
    l=[]
    while(num>0):
        l.append(num%10)
        num=num//10
    sum=0
    for i in range (len(l)):
        sum+=l[i]
    return sum 

while(temp>9):
    temp=add_digit(temp)
print(f"Sum of all digits upto sigle digit is {temp}")