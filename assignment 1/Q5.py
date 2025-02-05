def reverse_string(s):
    return s[::-1]

name = []
reverse_name = []


for i in range(10):
    a = input(f"Enter name {i+1}: ") 
    name.append(a)

for i in range(10):
    reversed_name = reverse_string(name[i])
    reverse_name.append(reversed_name)

print("Original names:", name)

print("Reversed names:", reverse_name)
