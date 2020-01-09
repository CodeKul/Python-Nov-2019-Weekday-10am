import numpy as np

a = np.array([1, 2, 3])

print(a)
print(type(a))
print(a.shape)

print(a[0])
print(a[1])
print(a[2])

a[0] = 5

print(a)


a = np.zeros((3,2)) # Create an array of all zeros
b = np.ones((3,3)) # Create an array of all ones
c = np.full((4,4), 122) # Create a constant array
d = np.eye(4) # Create a 2x2 identity matrix
e = np.random.random((3,2)) # Create an array filled with random values
print(e)

# Array indexing

# An exemplar array 
arr = np.array([[-1, 2, 0, 4], 
                [4, -0.5, 6, 0], 
                [2.6, 0, 7, 8], 
                [3, -7, 4, 2.0]]) 
print(arr)
# Slicing array 
temp = arr[1:3, 1:3] 
print ("Array with first 2 rows and alternate columns(0 and 2):\n", temp) 
  
# Integer array indexing example 
temp = arr[[0, 1, 2, 3], [3, 2, 1, 0]] 
print ("\nElements at indices (0, 3), (1, 2), (2, 1),"
                                    "(3, 0):\n", temp) 
  
# boolean array indexing example 
cond = arr > 0 # cond is a boolean array 
temp = arr[cond] 
print ("\nElements greater than 5:\n", temp) 

