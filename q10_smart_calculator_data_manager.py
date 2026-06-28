"""Q10. Smart Calculator & Data Manager mini project."""

import math
import random
from datetime import datetime


history = {}


def store_result(operation, result):
    """Store operation result with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    history[timestamp] = {
        "operation": operation,
        "result": result,
    }
    print("Result stored successfully.")


def basic_arithmetic():
    """Perform basic arithmetic operations."""
    try:
        first = float(input("Enter first number: "))
        second = float(input("Enter second number: "))

        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        choice = input("Choose operation: ")

        if choice == "1":
            result = first + second
            operation = f"{first} + {second}"
        elif choice == "2":
            result = first - second
            operation = f"{first} - {second}"
        elif choice == "3":
            result = first * second
            operation = f"{first} * {second}"
        elif choice == "4":
            if second == 0:
                print("Cannot divide by zero.")
                return
            result = first / second
            operation = f"{first} / {second}"
        else:
            print("Invalid arithmetic choice.")
            return

        print(f"Result: {result}")
        store_result(operation, result)

    except ValueError:
        print("Invalid input. Please enter numeric values.")


def scientific_calculations():
    """Perform scientific calculations using math module."""
    try:
        print("1. Square Root")
        print("2. Power")
        print("3. Factorial")
        choice = input("Choose scientific operation: ")

        if choice == "1":
            number = float(input("Enter number: "))
            if number < 0:
                print("Square root of negative number is not supported.")
                return
            result = math.sqrt(number)
            operation = f"sqrt({number})"
        elif choice == "2":
            base = float(input("Enter base: "))
            exponent = float(input("Enter exponent: "))
            result = math.pow(base, exponent)
            operation = f"pow({base}, {exponent})"
        elif choice == "3":
            number = int(input("Enter non-negative integer: "))
            if number < 0:
                print("Factorial is not defined for negative numbers.")
                return
            result = math.factorial(number)
            operation = f"factorial({number})"
        else:
            print("Invalid scientific choice.")
            return

        print(f"Result: {result}")
        store_result(operation, result)

    except ValueError:
        print("Invalid input for scientific calculation.")


def generate_random_numbers():
    """Generate random numbers using random module."""
    try:
        start = int(input("Enter start value: "))
        end = int(input("Enter end value: "))
        count = int(input("How many random numbers? "))

        if start > end:
            print("Start value must be less than or equal to end value.")
            return

        numbers = [random.randint(start, end) for _ in range(count)]
        print("Random Numbers:", numbers)
        store_result("Random Numbers", numbers)

    except ValueError:
        print("Invalid input. Please enter integers only.")


def store_custom_result():
    """Store a user-entered result in dictionary history."""
    operation = input("Enter operation name: ").strip()
    result = input("Enter result value: ").strip()

    if not operation or not result:
        print("Operation and result cannot be empty.")
        return

    store_result(operation, result)


def view_history():
    """Display stored history."""
    if not history:
        print("No history available.")
        return

    print("\nCalculation History")
    print("-" * 40)
    for timestamp, data in history.items():
        print(f"{timestamp} | {data['operation']} = {data['result']}")


while True:
    print("\nSmart Calculator & Data Manager")
    print("1. Basic Arithmetic")
    print("2. Scientific Calculations")
    print("3. Generate Random Numbers")
    print("4. Store Results in Dictionary")
    print("5. View History")
    print("6. Exit")

    menu_choice = input("Enter your choice: ")

    if menu_choice == "1":
        basic_arithmetic()
    elif menu_choice == "2":
        scientific_calculations()
    elif menu_choice == "3":
        generate_random_numbers()
    elif menu_choice == "4":
        store_custom_result()
    elif menu_choice == "5":
        view_history()
    elif menu_choice == "6":
        print("Thank you for using Smart Calculator & Data Manager.")
        break
    else:
        print("Invalid choice. Please select 1 to 6.")
