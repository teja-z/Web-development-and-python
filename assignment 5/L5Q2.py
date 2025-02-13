t=int(input("Enter number of test cases :"))
for i in range(t):
    k=int(input("Enter number of cuts:"))
    l=k//2
    b=k-l
    ans=l*b
    print(ans)