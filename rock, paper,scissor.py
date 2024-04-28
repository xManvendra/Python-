import random
while True:
    ch=input('Enter your guess : ')
    c=random.choice(['rock','paper','scissor'])
    if (ch=='rock' and c=='scissor') or (ch=='paper' and c=='rock') or (ch=='scissor' and c=='paper'):
        print('You Win, computer guess : ',c)
    elif ch==c:
        print('Match draw, computer guess : ',c)
    else:
        print('You Lose, computer guess : ',c)
    b=input('Enter yes to contiue and no to exit : ')
    if b=='yes':
        continue
    else:
        break
