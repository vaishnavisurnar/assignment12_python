"""Q6. Sets + Tuples + Modules."""

import math
import random


def unique_number_program():
    """Read 10 numbers, store unique values, and perform module operations."""
    unique_numbers = set()

    try:
        for count in range(1, 11):
            number = int(input(f"Enter number {count}: "))
            unique_numbers.add(number)

        number_tuple = tuple(unique_numbers)
        print("\nUnique Numbers Set:", unique_numbers)
        print("Tuple:", number_tuple)

        sample_count = min(3, len(number_tuple))
        random_numbers = random.sample(number_tuple, sample_count)
        print(f"{sample_count} Random Numbers:", random_numbers)

        total = sum(number_tuple)

        if total < 0:
            print("Cannot calculate square root because sum is negative.")
        else:
            print(f"Square Root of Sum ({total}): {math.sqrt(total):.2f}")

    except ValueError:
        print("Invalid input. Please enter integers only.")
    except Exception as error:
        print(f"Something went wrong: {error}")


unique_number_program()
