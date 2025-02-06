def reverse_string(s):
    return s[::-1]

t=int(input("Enter the number of cases :"));
for i in range (t):
    a=input("Enter the string:")
    b=reverse_string(a)
    sum=0
    for j in range(len(a)//2) :
        if(a[j]!=b[j]):
            sum=sum+abs(ord(a[i])-ord(b[i]))
    print(sum)