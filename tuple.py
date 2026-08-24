tup = (1, 2, 3)
print(type(tup))

print(min(tup))
print(len(tup))

tupA = (2, 'reddy', 6.9)
print(tupA)

num, numA, numB = tupA

print(num)
print(numA)
print(numB)

tupB = (34,'sridha', [1, 2, 3, 4])

tupB[2][1] = 18
print(tupB)  # Output: (34, 'sridha', [1, 17, 3, 4])

print(34 in tupB)  # Output: True
print(1 in tupB)  # Output: True