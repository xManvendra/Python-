bjp=cng=sapa=0
while True:
    name=input("Enter your Name :")
    age=int(input("Enter your age :"))
    if age>17:
        print("Enter your vote :")
        ch=input("BJP , CNG , SAPA :")
        if ch=='BJP':
            print("You voted to BJP ")
            bjp+=1
        elif ch=='CNG':
            print("You voted to CNG ")
            cng+=1
        elif ch=='SAPA':
            print("You voted to SAPA ")
            sapa+=1
        else:
            print("You entered wrong choice")
    else:
        print("You are not valid for voting")
    ch2=input("Enter your choice to continue or exit :")
    if ch2=='continue':
        continue
    else:
        if bjp>cng and bjp>sapa:
            print("BJP won")
        elif cng>sapa and cng>bjp:
            print('CNG won')
        else:
            print("SAPA won")
        break
