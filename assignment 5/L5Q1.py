l=int(input("Enter left limit 'L':"))
r=int(input("Enter right limit 'R':"))
x=[]
for i in range(l,r+1,1):
    for j in range(l,r+1,1):
        x.append(i^j)
k=max(x)
print(k)
