class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)


class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

    def show_marks(self):
        print("Marks:", self.marks)


student1 = Student("Reddy", 90)

student1.show_name()
student1.show_marks()