import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print("dimension",arr)
a = arr.ndim
print("the dimension is:\n",a)
b = arr.sum()
print("the sumis:\n",b)
c = arr.min()
print("the minimum is:\n",c)
d = arr.max()
print("the maximum is:\n",d)
e = arr.cumsum()
print("the cumlative frequency is:\n",e)
arr1 = arr+1
print("add  elements to the matrix:\n",arr1)
arr2 = arr-1
print("subtractig elements to the matrix:\n",arr2)
arr3 = arr**2
print("multiplication elements to the matrix :\n",arr3)
arr4 = arr**3
print("multiplication of cube elements to the matrix :\n",arr4)
arr5 = arr.max(axis=1)
print("max of array with axis",arr5)
arr6 = arr.min(axis=1)
print("min of array with axis",arr6)
arr7=arr.max()
print(arr7)






