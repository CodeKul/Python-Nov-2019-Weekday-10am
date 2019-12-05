# Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).

def create_square_list(a, b):
    l = []
    for no in range(a, b+1):
        l.append(no ** 2)
    return l

l1 = create_square_list(1, 30)
print(l1)