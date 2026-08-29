# Function Arguments in Python


# 1. Positional Arguments
def add(a, b):
    print("Sum:", a + b)


add(10, 20)


# 2. Multiple Positional Arguments
def student(name, age, marks):
    print("Name:", name)
    print("Age:", age)
    print("Marks:", marks)


student("Reddy", 21, 85)


# 3. Keyword Arguments
def employee(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)


employee(city="Bengaluru", name="Reddy", age=21)


# 4. Default Arguments
def greet(name="User"):
    print("Hello", name)


greet("Reddy")
greet()


# 5. Returning a value
def multiply(a, b):
    return a * b


result = multiply(10, 5)
print("Multiplication:", result)


# 6. Default + Positional Argument
def calculate(price, tax=18):
    total = price + (price * tax / 100)
    return total


print("Total:", calculate(1000))
print("Total with 10% tax:", calculate(1000, 10))