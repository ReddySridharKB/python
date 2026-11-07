
# class computer:
#     def config(self):
#         print("i5, 16gb, 1TB")

# com1 = computer()
# com2 = computer()

# com1.config()


class student:
    def __init__(self, name, age, dept, marks):
        self.name = name
        self.age = age
        self.dept = dept
        self.marks = marks

student1 = student("Manvi", 20, "TEX", 85)
student2 = student("Sridha", 21, "ECE", 92)

print("Name:", student1.name)
print("Age:", student1.age)
print("Department:", student1.dept)
print("Marks:", student1.marks)

print("------------------")

print("Name:", student2.name)
print("Age:", student2.age)
print("Department:", student2.dept)
print("Marks:", student2.marks)


class Employee:

    def __init__(self, name1, age, salary):
        self.name = name1
        self.age = age
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)


employee1 = Employee("Reddy", 21, 120000)
employee2 = Employee("Manvi", 20, 80000)

employee1.display()
employee2.display()
