sub=['English','Math','Physics','Chemistry','Computer']
while True:
    name=input("Enter the student name :")
    print("Enter the subject marks for :")
    marks=[]
    for i in sub:
        print(i,end=' ')
        mark=int(input(" :"))
        marks.append(mark)
    grade=(sum(marks)/500)*100
    if grade>89:
        print(name,' scored : A+ (',grade,')')
    elif grade>79:
        print(name,' scored : A (',grade,')')
    elif grade>69:
        print(name,' scored : B+ (',grade,')')
    elif grade>59:
        print(name,' scored : B (',grade,')')
    elif grade>39:
        print(name,' scored : C (',grade,')')
    else:
       print(name,' Failed : E (',grade,')')
    ch=input("Enter to continue or exit :")
    if ch=='continue':
        continue
    else:
        break
