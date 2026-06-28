"""Q3. Lists + Functions + Exception Handling."""


def manage_marks():
    """Read 5 subject marks and display statistics."""
    marks = []

    for subject_no in range(1, 6):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {subject_no}: "))

                if mark < 0 or mark > 100:
                    print("Marks must be between 0 and 100.")
                    continue

                marks.append(mark)
                break

            except ValueError:
                print("Invalid input. Please enter numeric marks only.")

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)
    sorted_marks = sorted(marks, reverse=True)

    print("\nMarks List:", marks)
    print(f"Average Marks: {average:.2f}")
    print(f"Highest Marks: {highest}")
    print(f"Lowest Marks: {lowest}")
    print("Marks in Descending Order:", sorted_marks)


manage_marks()
