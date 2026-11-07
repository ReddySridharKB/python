

def square(num):
    return num * num

def cube(num):
    return num * num * num  

def operation(func, value):
    return func(value)

value = 5
result = operation(square, value)
print(result)