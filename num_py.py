import numpy as np

arr1 = np.array([1,2,3,4,5]) # 1d array
print(arr1)
print(type(arr1))

# arr2 = np.array([1,2,3,4,5]) 
# arr2.reshape(1,5) # reshaping 1d array to 2d array
# print(arr2)
# print(arr2.shape)

arr2 = np.array([[1,2,3,4,5],[6,7,8,9,10]]) # 2d array
print(arr2)
print(arr2.shape)


arr3 = np.arange(0,10) # creates an array given range, can also have optional parameter i.e. step np.arrange(0,10,2) -> which skips one number like 0,2,4,6,8
print(arr3)

ones_arr = np.ones((3,4)) # creates an array with one's 
print(ones_arr)

identity_matrix = np.eye(3) # creates an identity matrix
print(identity_matrix)

# numpy vectorized operations

list1 = np.array([1,2,3,4,5])
list2 = np.array([10,20,30,40,50])
# numpy will do the operations index wise
print(f"Addition: {list1+list2}")
print(f"Subtraction: {list1-list2}")
print(f"Multiplication: {list1*list2}")
print(f"Division: {list1/list2}")

# universal  functions

print(np.sqrt(list2))
print(np.exp(list2))
print(np.sin(list2))
print(np.log(list2))


# array slicing and indexing

array = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(array)

# printing row 1, column 1
print(array[0][0])
# printing 7,8,11,12
print(array[1:,2:])

print(array[1:,1:3])

#modifying elements
array[0,0] = 100
print(array) 

# statistics functions
arr = np.array([1,2,3,4,5,6,7,8,9,10])

print(f"Mean: {np.mean(arr)}")
print(f"Variance: {np.var(arr)}")
print(f"Standard Deviation: {np.std(arr)}")
print(f"Median: {np.median(arr)}")


# logical operations
print(arr[arr>5])

print(arr[(arr >= 5) & (arr<=8) ])
