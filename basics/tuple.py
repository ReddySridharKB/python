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

my_tuple = (1, 2, 3, 4, 5, 1)

print(my_tuple[0])      # indexing
print(my_tuple[-1])     # negative indexing
print(my_tuple[1:3])    # slicing

print(len(my_tuple))    # length

print(my_tuple.count(1))   # count how many times 1 appears
print(my_tuple.index(4))   # position of 4