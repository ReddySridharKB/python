# Python List Operations

numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)

# Indexing
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Slicing
print("First three:", numbers[:3])

# Add
numbers.append(60)
print("After append:", numbers)

numbers.insert(1, 15)
print("After insert:", numbers)

numbers.extend([70, 80])
print("After extend:", numbers)

# Remove
numbers.remove(30)
print("After remove:", numbers)

numbers.pop()
print("After pop:", numbers)

# Information
print("Length:", len(numbers))
print("Count of 20:", numbers.count(20))
print("Position of 40:", numbers.index(40))

# Membership
print("Is 40 present?", 40 in numbers)

# Sort
numbers.sort()
print("Sorted:", numbers)

# Reverse
numbers.reverse()
print("Reversed:", numbers)