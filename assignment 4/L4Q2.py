import math
t=int(input("Enter test cases:"))
for i in range(t):
    a=int(input())
    b=int(input())
    a1=int(math.sqrt(a))
    b1=int(math.sqrt(b))
    k=0
    for a1 in range(b1+1):
        if a1*a1<=b and a1*a1>=a:
            k+=1
    print(k)     