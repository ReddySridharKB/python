class Abc:
    def __new__(cls):
        print("Constructor is called")
        return super().__new__(cls)

    def __init__(self):
        print("Init method is called")

    def show(self):
        print("Show method is called")

obj1 = Abc()
obj1.show()

obj2 = Abc.__new__(Abc)
obj2.__init__()
obj2.show()