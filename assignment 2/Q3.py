t=int(input())
for i in range(t):
    n=int(input());
    temp=n
    l=[]
    while temp!=0:
       a=temp%10
       temp=temp//10
       #print(temp)
       l.append(a) 
    k=0
    for i in range(len(l)):
        if n%l[i]==0:
            k=k+1
    print(k)
    #print("\n")
