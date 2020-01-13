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



# Basic operations

a = np.array([1, 2, 5, 3]) 

# add 1 to every element 
print ("Adding 1 to every element:", a+1) 
  
# subtract 3 from each element 
print ("Subtracting 3 from each element:", a-3) 
  
# multiply each element by 10 
print ("Multiplying each element by 10:", a*10) 
  
# square each element 
print ("Squaring each element:", a**2) 
  
# modify existing array 
a *= 2
print ("Doubled each element of original array:", a) 

# transpose of array 
a = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]]) 
  
print ("\nOriginal array:\n", a) 
print ("Transpose of array:\n", a.T) 

arr = np.array([[1, 5, 6], 
                [4, 7, 2], 
                [3, 1, 9]]) 
  
# maximum element of array 
print ("Largest element is:", arr.max()) 
print ("Row-wise maximum elements:", 
                    arr.max(axis = 1)) 
  
# minimum element of array 
print ("Column-wise minimum elements:", 
                        arr.min(axis = 0)) 
  
# sum of array elements 
print ("Sum of all array elements:", 
                            arr.sum()) 
  
# cumulative sum along each row 
print ("Cumulative sum along each row:\n", 
                        arr.cumsum(axis = 1)) 

a = np.array([[1, 2], 
            [3, 4]]) 
b = np.array([[4, 3], 
            [2, 1]]) 
  
# add arrays 
print ("Array sum:\n", a + b) 
  
# multiply arrays (elementwise multiplication) 
print ("Array multiplication:\n", a*b) 
  
# matrix multiplication 
print ("Matrix multiplication:\n", a.dot(b)) 


# Universal functions (ufunc):NumPy provides familiar mathematical functions such as sin, cos, exp, etc.

# create an array of sine values 
a = np.array([0, np.pi/2, np.pi]) 
print ("Sine values of array elements:", np.sin(a)) 
  
# exponential values 
a = np.array([0, 1, 2, 3]) 
print ("Exponent of array elements:", np.exp(a)) 
  
# square root of array values 
print ("Square root of array elements:", np.sqrt(a)) 


# Sorting array:

a = np.array([[1, 4, 2], 
              [3, 4, 6], 
              [0, -1, 5]]) 
  
# sorted array 
print ("Array elements in sorted order:\n", 
                    np.sort(a, axis = None)) 
  
# sort array row-wise 
print ("Row-wise sorted array:\n", 
                np.sort(a, axis = 1)) 
  
# specify sort algorithm 
print ("Column wise sort by applying merge-sort:\n", 
            np.sort(a, axis = 0, kind = 'mergesort')) 
  
# Example to show sorting of structured array 
# set alias names for dtypes 
dtypes = [('name', 'S10'), ('grad_year', int), ('cgpa', float)] 
  
# Values to be put in array 
values = [('Hrithik', 2009, 8.5), ('Ajay', 2008, 8.7),  
           ('Pankaj', 2008, 7.9), ('Aakash', 2009, 9.0)] 
             
# Creating array 
arr = np.array(values, dtype = dtypes) 
print ("\nArray sorted by names:\n", 
            np.sort(arr, order = 'name')) 
              
print ("Array sorted by grauation year and then cgpa:\n", 
                np.sort(arr, order = ['grad_year', 'cgpa'])) 