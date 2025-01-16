t = int(input())  
for _ in range(t):
    n = int(input())
    x = int(input())
    s = int(input()) 
    
    arr = [0] * n
    arr[x - 1] = 1
    
    for _ in range(s):
        a = int(input())
        b = int(input())  
        arr[a - 1], arr[b - 1] = arr[b - 1], arr[a - 1]
    
    for i in range(n):
        if arr[i] == 1:
            print(i + 1)  
            break
