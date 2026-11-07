set1 = {23, 56, 78, 21, 56}
print(set1)

print(23 in set1)  # Output: True

print(len(set1))  # Output: 4

print(type(set1))  # Output: <class 'set'>

set2 = {}
print(type(set2))  # Output: <class 'dict'>

set2 = set()
print(type(set2))  # Output: <class 'set'>

set2 = set('abcdteh')
set3 = set('aeiouv')

print(set2 - set3)
print(set2 | set3)
print(set2 & set3)