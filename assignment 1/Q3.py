#convert from feet into inches, yards, miles, millimeters, centimeters,
#meters, or kilometers.

a=int(input("Enter the value in feet "))
print("1.Inches")
print("2.Yards")
print("3.Miles")
print("4.millimeters")
print("5.centimeters")
print("6.meters")
print("7.kilometers")
b=int(input("Enter serial number of operation given following:"))
l=[]
l.append(a*12)
l.append(a*0.333333)
l.append(a*0.000189394)
l.append(a*304.8)
l.append(a*30.48)
l.append(a*0.3048)
l.append(a*0.0003048)
print(l[b-1])
