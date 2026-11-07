class Bank:

    bank_name = "SBI"

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def display(self):
        print("Bank Name:", Bank.bank_name)
        print("Account Holder:", self.account_holder)
        print("Balance:", self.balance)

    @classmethod
    def change_bank(cls, bank_name):
        cls.bank_name = bank_name

    @staticmethod
    def is_valid_balance(balance):
        return balance >= 0

acc1 = Bank("Reddy", 1000)
acc2 = Bank("Manvi", 2000)
acc1.display()
acc2.display()

Bank.change_bank("KBL")

acc1.display()
acc2.display()

print("Is valid balance:", Bank.is_valid_balance(500))
print("Is valid balance:", Bank.is_valid_balance(-100))

print("--------------------------------------")


class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)

student1 = Student("Reddy", 21, 85)
student2 = Student("Manvi", 20, 92)

student1.display()
student2.display()