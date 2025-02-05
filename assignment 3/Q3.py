t=int(input("Enter number of test cases:"))
for i in range(t):
    n=int(input("Enter number of grow cycles:"))
    ans=1
    for i in range(n):
        if i%2==0:
            ans*=2
        else:
            ans+=1
    print(ans)