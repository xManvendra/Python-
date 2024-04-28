f=open("C:\\Users\\kasib\\OneDrive\\Documents\\codes\\report.txt","w")
sub=['English','Math','Physics','Chemistry','Computer']
while True:
    name=input("Enter the student name :")
    f.write("Students Name : "+str(name))
    print("Enter the subject marks for :")
    f.write("\nMarks for subjects :")
    marks=[]
    for i in sub:
        print(i,end=' ')
        mark=int(input(" :"))
        f.write('\n'+str(i)+" : "+str(mark))
        marks.append(mark)
    grade=(sum(marks)/500)*100
    f.write("\nTotal marks Scored :"+str(sum(marks)))
    if grade>89:
        print(name,' scored : A+ (',grade,')')
        f.write("\nPercentage Scored : "+str(grade))
    elif grade>79:
        print(name,' scored : A (',grade,')')
        f.write("\nPercentage Scored : "+str(grade))
    elif grade>69:
        print(name,' scored : B+ (',grade,')')
        f.write("\nPercentage Scored : "+str(grade))
    elif grade>59:
        print(name,' scored : B (',grade,')')
        f.write("\nPercentage Scored : "+str(grade))
    elif grade>39:
        print(name,' scored : C (',grade,')')
        f.write("\nPercentage Scored : "+str(grade))
    else:
       print(name,' Failed : E (',grade,')')
       f.write("\nPercentage Scored : "+str(grade))
    ch=input("Enter to continue or exit :")
    if ch=='continue':
        continue
    else:
        f.close()
        break
