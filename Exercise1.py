l1 = [12, 45, 88, 23, 79, 23, 89, 12, 78, 34, 47, 28]
sum = 0
l = len(l1) - 1
while l >= 0:
    sum += l1[l]
    l -= 1

print('Sum of all elements:', sum)

sum = 0
for no in l1:
    sum += no

print('Sum of all elements:', sum)


sum_odd = 0
sum_even = 0

for no in l1:
    if no % 2 == 0:
        sum_even += no
    else:
        sum_odd += no

print("Even sum:", sum_even)
print('Odd sum:', sum_odd)