R=list()
for i in range (0,5):
    L=list()
    for j in range(i,101,5):
        L.append(j)
    R.append(L)
del(R[0][0])
print(R)
Union=[]
for i in range(1,5):
    Union+=R[i]
print(Union)