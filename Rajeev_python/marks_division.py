a=int(input("Enter the marks obtain in physics"))
b=int(input("Enter the marks obtain in Chameatry"))
c=int(input("Enter the marks obtain in maths"))
d=int(input("Enter the marks obtain in Hindi"))
p=float((a+b+c+d)/4)
print(p)
if p>=90:
    print("division first")
elif p<=60:
    print("division second")