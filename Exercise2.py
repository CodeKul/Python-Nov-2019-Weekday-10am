# Write a Python program to get the largest number from a list.

l1 = [-37, -26, -13, -85, -23, -84, -56, -34, -67, -26]

max_no = l1[0]

for no in l1:
    if no > max_no:
        max_no = no

print('Max:', max_no)