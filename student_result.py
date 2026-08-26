import math

# Student information
name = input("Enter your name: ")
branch = input("Enter your branch: ")

# Get marks
python = int(input("Enter Python marks: "))
sql = int(input("Enter SQL marks: "))
dsa = int(input("Enter Data Structures marks: "))

# Store marks in a dictionary
marks = {
    "python": python,
    "sql": sql,
    "dsa": dsa
}

# Calculate total and average
total = python + sql + dsa
average = total / 3

print("\n----- STUDENT RESULT -----")
print("Name:", name)
print("branch:", branch)
print("Marks:", marks)
print("Total:", total)
print("Average:", round(average, 2))

# Result checking
if average >= 50:
    print("Result: PASS")

    if average >= 75:
        print("Grade: A")
    elif average >= 60:
        print("Grade: B")
    else:
        print("Grade: C")

else:
    print("Result: FAIL")

# Using math module
print("Rounded average:", math.floor(average))