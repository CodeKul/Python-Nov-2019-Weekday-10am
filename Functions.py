def my_function():
    print('This is my function')

my_function()

def function_with(param):
    print('This is param:', param)

function_with('Codekul')

def function_with_multiple(a, b=20, c=10):
    print('a:',a)
    print('b:',b)
    print('c:',c)

function_with_multiple(10,c=30)

def function_returning():
    str1 = "Codekul"
    return str1

s = function_returning()
print(s)

print(function_returning())


def change_this(a):
    a = 100
    print('a:',a)

b = 10
change_this(b)
print('b:', b)

def change_list(l1):
    print('id(l1) before:', id(l1))
    l1.append(6)
    # l1 = [1,2,3,4,5,6]
    print('id(l1) after:', id(l1))
    print('l1:',l1)

l2 = [1,2,3,4,5]
print('id(l2) before:', id(l2))
change_list(l2)
print('id(l2) after:', id(l2))
print('l2:',l2)