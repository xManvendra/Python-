import random
c=u=0
while True:
    user=int(input("Enter your number you get on dice :"))
    u+=user
    comp=random.randint(1,6)
    c+=comp
    print("Computer dice roll :",comp)
    ch=input("Enter continue or exit :")
    if ch=='continue':
        continue
    elif ch=='exit':
        if c>u:
            print("Computer won by :",(c-u))
        elif c<u:
            print("User won by :",(u-c))
        else:
            print('Match draw ')
        break
    else:
        print("Invalid input")
        break
