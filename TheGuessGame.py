import random


while True:
    no1 = int(input('Enter a number: '))
    if no1 > 10 or no1 < 1:
        if no1 == 0:
            print('Bye!')
            break
        print('Enter a number between 1 and 10')
        continue

    no2 = random.randint(1, 10)

    if no1 == no2:
        print('You won!')
    else:
        print('Better luck next time!')