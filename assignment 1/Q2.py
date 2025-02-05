import random
l=[]
for _ in range(100):
    l.append(random.randint(0,1))
max=0
length=0
for i in range(100):
    if l[i]==0:
        length+=1
    else:
        if length>max:
            max=length
        length=0       
if length>max:
            max=length
print(l)      
print(max)    
