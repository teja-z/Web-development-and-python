def cheak_fibo(num):
    l=[0,1]
    value =0
    i=1
    while l[-1]<num:
        l.append(l[-1]+l[-2])
        if num in l:
            value=1
    return value  
t=int(input("Enter number of test cases"))
for i in range(t):
    n=int(input("Enter the number that you want to check:"))
    if cheak_fibo(n):
        print("Your number IsFibo")
    elif n==0 or n==1:
        print("Your number IsFibo")
    else:
        print("Your number IsNotFibo")