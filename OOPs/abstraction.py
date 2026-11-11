
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):

    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):

    def __init__(self, hours, hourly_rate):
        self.hours = hours
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours * self.hourly_rate


class Intern(Employee):
    def calculate_salary(self):
        print("Interns do not receive a salary.")

e3 = Intern()


e1 = FullTimeEmployee(50000)
e2 = PartTimeEmployee(100, 200)

print("Full-time salary:", e1.calculate_salary())
print("Part-time salary:", e2.calculate_salary())
e3.calculate_salary()
