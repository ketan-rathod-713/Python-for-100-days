import numpy as np

arr = np.array([1,2,3,4])

print(type(arr))

print(arr)

print(arr.shape) # (4,)

# arr[0] = "st" # It will give error as only same datatypes accepted in numpy

print(np.sum(arr[:2]))

arr2 = np.full((2,2), 10)

print(arr2)

print(arr2.shape)