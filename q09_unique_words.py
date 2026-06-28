"""Q9. Strings + Sets + Exception Handling + Modules."""

import math


try:
    sentence = input("Enter a sentence: ").strip()

    if not sentence:
        raise ValueError("Sentence cannot be empty.")

    words = sentence.lower().split()
    unique_words = set(words)
    sorted_words = sorted(unique_words)
    total_unique_words = len(unique_words)

    print("Unique Words in Sorted Order:", sorted_words)
    print(f"Total Unique Words: {total_unique_words}")
    print(f"Total Unique Words Power 2: {math.pow(total_unique_words, 2):.0f}")

except ValueError as error:
    print(f"Invalid input: {error}")
except Exception as error:
    print(f"Something went wrong: {error}")
