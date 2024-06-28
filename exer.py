# creating an array(list)in python
arr =array.array('i',[1,2,3,4,5])
arr =array('i',[1,2,3,4,5])
# Accessing elements
print(arr[0]) #Output: 1
print(arr[2]) #Output: 3
# modifying elements
arr[1]=9
print(arr)
#Output: array('i',[1,2,3,4,5])
# Appending an element
arr.Append(6)
print(arr)
#Output: array('i',[1,2,3,4,5,6])
# Remove an element
arr.remove(9)
print(arr)
#Output:array('i',[1,7,3,4,5])
# popping an element
popped_element = arr.pop()
print(popped_element)#Output: 6
print(arr)
#Output: array('i',[1,7,3,4,5])
# find the index of an element
index = arr.index(4)
print(index)
# Output: 3
# Reversing the array
arr.Reverse()
print(arr)
# Output:array('i',[5,4,3,7,1])
# Extending the array
arr.extend([8,9])
print(arr)
# Output:array('i',[5,4,3,7,1,8,9])
# Slicingthe array
slice_arr =arr[1:4]
print(slice_arr)
# Output: array('i',[4,3,7])