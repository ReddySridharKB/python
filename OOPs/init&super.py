class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

m1 = manager("John", 50000, "Sales")
print(m1.name)
print(m1.salary)
print(m1.department)