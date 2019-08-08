from numpy import *
arr=array([
    [1,2,3],[4,5,6]
])
print(arr.transpose())
print(arr.flatten())

arr1=array([1,2,3])
arr2=array([4,5,6])
arr3=array([7,8,9])
print(concatenate(arr1,arr2,arr3))
print(concatenate(arr1,arr2),axis=1)
