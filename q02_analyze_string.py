"""Q2. Strings + Loops + Functions."""


def analyze_string(s):
    """Analyze length, reverse, vowels, and indexes of a string."""
    if not s:
        print("Empty string entered. Please enter a valid string.")
        return

    vowels = "aeiou"
    vowel_count = 0

    print(f"Original String: {s}")
    print(f"Length: {len(s)}")
    print(f"Reverse: {s[::-1]}")

    for char in s:
        if char.lower() in vowels:
            vowel_count += 1

    print(f"Number of vowels: {vowel_count}")
    print("\nCharacter Index Details:")

    for index in range(len(s)):
        negative_index = index - len(s)
        print(f"Character: {s[index]}, Positive Index: {index}, Negative Index: {negative_index}")


user_string = input("Enter a string: ")
analyze_string(user_string)
