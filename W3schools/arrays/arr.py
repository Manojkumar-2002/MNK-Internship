from array import array

arr = array('i', [1, 3, 5, 7, 9])
arr.append(11)
print("New array:", arr)

arr = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
arr.reverse()
print("Reversed array:", arr)

arr = array('i', [1, 3, 5, 7, 9])
print("Length in bytes of one array item:", arr.itemsize)

arr = array('i', [1, 3, 5, 7, 9])
print("Memory address and length in elements:", arr.buffer_info())

arr = array('i', [1, 3, 5, 3, 7, 9, 3])
print("Occurrences of 3:", arr.count(3))

arr = array('i', [1, 3, 5, 7, 9])
arr.extend([1, 3, 5, 7, 9])
print("Extended array:", arr)

arr = array('u', 'w3resource')
bytes_representation = arr.tobytes()
print("Bytes to String:", bytes_representation)

lst = [1, 2, 6, -8]
arr = array('i', lst)
print("Items in the array:", arr)

arr = array('i', [1, 3, 5, 7, 9])
arr.insert(1, 4)
print("New array after insertion:", arr)

arr = array('i', [1, 3, 5, 7, 9])
del arr[2]
print("New array after deletion:", arr)

arr = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
arr.remove(3)
print("New array after remove:", arr)

arr = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
lst = arr.tolist()
print("Array to list:", lst)

arr = array('i', [1, 2, 3, 4, 5])
print(any(arr.count(x) > 1 for x in arr))

arr = array('i', [1, 2, 3, 4, 5, 2])
print(any(arr.count(x) > 1 for x in arr))

arr = array('i', [1, 2, 3, 1])
print(any(arr.count(x) > 1 for x in arr))
