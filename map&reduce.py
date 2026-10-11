from functools import reduce

def square(n):
    return n * n

def add(a, b):
    return a + b

numbers = [1, 2, 3, 4, 5]

# Using map()
squares = list(map(square, numbers))
print("Squares:", squares)

# Using reduce()
total = reduce(add, squares)
print("Sum:", total)