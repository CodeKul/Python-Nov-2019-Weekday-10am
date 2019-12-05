# Write a Python function to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9] 
# Expected Result : [2, 4, 6, 8]

def get_even(l):
    list1 = []
    for no in l:
        if no % 2 == 0:
            list1.append(no)
    return list1


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = get_even(l1)
print(l2)