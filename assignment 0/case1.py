n=int(input("number or person in queue:"))
L=[]
count=0

print("enter heights of person in queue order")
#taking input height of each person
for i in range(0,n,1):
    a=int(input())
    L.append(a)
for i in range(0,n,1):
    min=L[i]
    index=i
    for j in range(i+1,n,1):
        if(min>L[j]):
            min=L[j]
            index=j
    if(i!=index):
        c=L[i]
        L[i]=L[index]
        L[index]=c
        count+=1
    else:
        continue
print(L)
print(count)