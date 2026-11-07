add = lambda a, b: a + b
print("Sum:", add(10, 20))


students = [("Ravi", 85), ("Reddy", 92), ("Rahul", 76), ("Kiran", 89)]

get_grade = lambda marks: "Pass" if marks >= 35 else "Fail"

for name, marks in students:
    print("Name:", name)
    print("Marks:", marks)
    print("Result:", get_grade(marks))
    print("----------")
