while True:
    n1=int(input("Enter first number :"))
    n2=int(input("Enter second number :"))
    op=input("Enter -, +, *, /, %(for remainder) :")
    if op=='-':
        print(n1-n2)
    elif op=='+':
        print(n1+n2)
    elif op=='*':
        print(n1*n2)
    elif op=='/':
        print(n1/n2)
    elif op=='%':
        print(n1%n2)
    else:
        print("Invalid input ")
    ch=input("Enter 'exit' to exit from programme :")
    if ch=='exit':
        break
    else:
        continue
