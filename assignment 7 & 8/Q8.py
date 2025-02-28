def decode(s, i=0, res=""): 
    if i == len(s):
        print(res)
        return
    if i < len(s) and s[i] != "0":
        decode(s, i + 1, res + chr(int(s[i]) + 64))
    if i + 1 < len(s) and s[i] != "0" and 10 <= int(s[i:i+2]) <= 26:
        decode(s, i + 2, res + chr(int(s[i:i+2]) + 64))

s = input("Enter a string of numbers to decode: ")
decode(s)