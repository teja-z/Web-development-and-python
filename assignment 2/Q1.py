word = input("Enter any word:")
str=""
for i in range(len(word)):
    if(i+1)%2==0:
        str=str+word[i].upper()
    else:
        str=str+word[i].lower()

print(str)