alphabets = "abcdefghijklmnopqrstuvwxyz"
flag = 1
a = str(input("Enter the input:")).lower()

for i in alphabets:
    if i not in a:
        flag = 0
        break

if flag:
    print("pangram")
else:
    print("not pangram")
