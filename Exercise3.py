# Write a progran to remove numbers from a string
# E.g. Input: Python-Nov-2019-Weekday-10am
# Output: Python-Nov--Weekday-am

str1 = input('Enter a string: ')

l = len(str1) - 1
i = 0
while i < l:
    if str1[i].isdigit():
        str1 = str1.replace(str1[i], '', 1)
        l -= 1
        continue
    i += 1

print(str1)