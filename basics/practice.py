# Practical Function Arguments Example

def calculate_total(numbers):
    return sum(numbers)


def calculate_average(numbers):
    return sum(numbers) / len(numbers)


def show_summary(name, numbers):
    total = calculate_total(numbers)
    average = calculate_average(numbers)

    print("\n--- Data Summary ---")
    print("Name:", name)
    print("Data:", numbers)
    print("Total:", total)
    print("Average:", round(average, 2))


# Data
sales = [100, 250, 150, 300, 200]

# Passing arguments to the function
show_summary("January Sales", sales)