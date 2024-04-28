sp=int(input("Enter starting point :"))
ep=int(input("Enter ending point :"))
up=int(input("Enter updation :"))
ch1=input("Enter choice for forward or reverse printing :")
ch2=input("Enter choice for vertical or horizontal print :")
if ch1=='forward':
    for i in range(sp,ep,up):
        if ch2=='horizontal':
            print(i,end=' ')
        elif ch2=='vertical':
            print(i)
        else:
            print("Second choice invalid")
elif ch1=='reverse':
    for i in range(ep,sp,-(up)):
        if ch2=='horizontal':
            print(i,end=' ')
        elif ch2=='vertical':
            print(i)
        else:
            print("Second choice invalid")
else:
    print("First choice invalid")
