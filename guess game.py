import random as r

while True:
    n = int(input("Enter a range: "))
    c = r.randrange(0, n)
    y = int(input("Enter the number: "))
    if (y == c):
        print("Congratulation the number was:", c)
    else:
        print("Better luck next time.")
    ch=input("Enter 'exit' to end game :")
    if ch=='exit':
        break
    else:
        continue

