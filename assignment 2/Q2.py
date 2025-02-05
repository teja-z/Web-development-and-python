dict={}
while(True):
    item=input("Enter item name:")
    dict[item]=int(input("Enter price:"))
    choice=int(input("press 1 to enter more items or 0 to exit:"))
    if(choice==0):
        break
print(dict)
while(True):
    item=input("Enter item name to check:")
    if item in dict:
        print(item,dict[item],sep=':')
    else:
        print(item,"not in stock")
    choice=int(input("wanna check another item press 1 else press 0:\n"))
    if(choice==0):
        break