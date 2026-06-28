"""Q7. Lambda + range() + Lists + Exception Handling."""


try:
    square = lambda number: number * number

    numbers = range(1, 21)
    squares = [square(number) for number in numbers]
    even_squares = [value for value in squares if value % 2 == 0]

    print("Numbers from 1 to 20:", list(numbers))
    print("Squares:", squares)
    print("Even Squares:", even_squares)

except Exception as error:
    print(f"Something went wrong: {error}")
