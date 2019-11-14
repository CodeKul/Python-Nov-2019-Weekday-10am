# str

str1 = "Codekul"
str2 = 'Codekul'
# 'Codekul' - "The Gurukul for Coders"!
str3 = """'Codekul' - "The Gurukul for Coders"!"""
str4 = """Codekul
    The
        Gurukul
            for
                Coders!"""

str5 = "Best training institute: " + str1

print(str1)
print(str2)
print(str3)
print(str4)
print(str5)
a = 11
print("Python: %s %dam"%(str1, a))
print("a: {}".format(a))

str6 = "Pune's {} {}".format(str5, 'Private Limited')
print(str6)


# list

list1 = [1,2,3,4,5,6,7,8,9]
print(list1[7])

list2 = [1, 2, 3, 'Four', 'Five', 6.7, True, list1]
print(list2[5])

list3 = list1 + list2

print(list3)
print(type(list3))

# Dict

dict1 = {'One': 1, 'Two': 2, 'Three': True, 10: False, 10: 'Ten'}
print(dict1[10])

# Tuple
t1 = (1,2,3,4,5)
print(t1)

list1.append(10)
list1.remove(4)
print(list1)

t1.append(6)
print(t1)