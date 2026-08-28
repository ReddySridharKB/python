# Break and Continue

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

for number in numbers:

    # Skip even numbers
    if number % 2 == 0:
        continue

    # Stop when number reaches 7
    if number == 7:
        break

    print("Number:", number)