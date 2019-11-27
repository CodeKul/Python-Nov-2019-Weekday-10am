def calc_fact(no):
    fact = 1
    while no > 1:
        fact *= no
        no -= 1
    return fact

no = 0
try:
    no = int(input('Enter a number: '))
except Exception as e:
    print(e)
    print('Please enter valid integer number!')
else:
    print('execute this if no any exception occured')
    print('Factorial:', calc_fact(no))
finally:
    print('This will execute all the time')

