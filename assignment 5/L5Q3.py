t=int(input("Enter number of test cases :"))
for i in range(t):
    a=input("Enter the string :")
    s=''.join(sorted(a,reverse=True))
    if a==s:
        print("no answer")
    else:
        print(s)