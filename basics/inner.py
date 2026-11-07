def outer():
    a = 10
    b = 20

    def inner():
        print(a + b)

    inner()

outer()