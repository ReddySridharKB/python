


try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    c = a / b
    print("Result:", c)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Invalid input. Please enter numeric values.")

except Exception as e:
    print("Error:", e)

else:
    print(" else block: Division was successful.")

finally:
    print("finally block: Execution of the try-except block is complete.")

print("Program continues after handling the exception.")