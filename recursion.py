import sys
sys.setrecursionlimit(1000)
print(sys.getrecursionlimit())

count = 1
def greet():
    global count
    print("Hello, World!", count)
    count += 1
    greet()
greet()