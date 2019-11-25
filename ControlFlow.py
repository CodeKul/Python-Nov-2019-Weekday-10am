'''
    if condition:
        statement1
        statement2
    else:
        statements
'''

a = 30
b = 20

if a < b:
    print('a is less than b')
elif a == b:
    print('a and b both are equal')
else:
    print('a is greater than b')

if a < b:
    print('a is less than b')
else:
    if a == b:
        print('a and b both are equal')
    else:
        print('a is greater than b')

if a < 30:
    print('Value of a: ',a)
    print('abcd')

# Loops

# print('Codekul')
# print('Codekul')
# print('Codekul')
# print('Codekul')
# print('Codekul')
# print('Codekul')
# print('Codekul')
# print('Codekul')
# print('Codekul')
# print('Codekul')

'''
    init
    while condition:
        statements
        incr/decr
'''

i = 0
while i < 10:
    if i % 2 == 0:
        print('Codekul')
    else:
        print('The Gurukul for Coders!')
    i += 1

i = 0
while i < 10:
    if i == 5:
        i += 1
        continue
    print('Codekul-Python:',i)
    i += 1

'''
    for item in collection:
        statements
'''

for ch in 'Codekul':
    print(ch)

l1 = [34, 56, 46, 72, 47, 23, 11]

for no in l1:
    if no % 7 == 0:
        print(no)