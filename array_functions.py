from array import array

numbers = array('i', [10, 20, 30, 40])

print("Original:", numbers)

numbers.append(50)
print("After append:", numbers)

numbers.extend([60, 70])
print("After extend:", numbers)

numbers.insert(1, 15)
print("After insert:", numbers)

numbers.remove(30)
print("After remove:", numbers)

numbers.pop()
print("After pop:", numbers)

print("Length:", len(numbers))
print("Index of 40:", numbers.index(40))
print("Count of 20:", numbers.count(20))

numbers.reverse()
print("Reversed:", numbers)

print("As list:", numbers.tolist())