#Import numpy into the system 
import numpy as np
#standard array
arr = np.array([1,2,3,4,5])
print(arr)
#Creating an array via a tuple
arr = np.array((1,2,3,4,5,6))
print(arr)

#0-D array
arr = np.array(42)
print(arr)

#1-D array
arr = np.array([1,2,3,4,5])
print (arr)

#2-D array
arr = np.array([[1,2,3],
               [4,5,6]])
print(arr)

#3-D array
arr = np.array([[[1,2,3],
               [4,5,6]],
               [[1,2,3],
                [4,5,6]]])

#creating multiple arrays using.ndim()function
a = np.array(42)
b = np.array ([1,2,3,4,5])
c = np.array ([[1,2,3], [4,5,6]])
d = np.array ([[1,2,3], [4,5,6]],
              [[6,7,8], [4,5,6]]])


print(a.ndim) 
print(b.ndim) 
print(c.ndim) 
print(d.ndim)  




