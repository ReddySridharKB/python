data = {0: 34, 1: 35, 2: 36, 3: 37}
print(data[1])

data1 = {'sss': 1432, 'reddy': 1433, 'sridha': 1434}
print(data1.get('sss'))

print(data1.get('sri', 'notfound'))

data1 = {'sss': 1432, 'reddy': 1433, 'sridha': 1434, 'sss':1433}
print(data1)

keys = {'sss', 'reddy', 'sridha'}
values = [1,2,3]
dict1 = dict(zip(keys, values))
print(dict1)

#popping
data1.pop('reddy')
print(data1)

del data1['sss']
print(data1)

#dict inside a dict
student = {"name": "Reddy", "marks": {"python": 90, "sql": 85}}

print(student["name"])
print(student["marks"])
print(student["marks"]["python"])