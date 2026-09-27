from array import array

numbers = array('i', [10, 20, 30, 40])

print("Original:", list(numbers))

numbers.append(50)
print("After append:", list(numbers))

numbers.extend([60, 70])
print("After extend:", list(numbers))

numbers.insert(1, 15)
print("After insert:", list(numbers))

numbers.remove(30)
print("After remove:", list(numbers))

numbers.pop()
print("After pop:", list(numbers))

print("Length:", len(numbers))
print("Index of 40:", numbers.index(40))
print("Count of 20:", numbers.count(20))

numbers.reverse()
print("Reversed:", list(numbers))

arr1 = array('i', [1, 2, 3])
arr2 = array('i', arr1.tolist())

arr1[2]= 18

print(arr1)
print(arr2)