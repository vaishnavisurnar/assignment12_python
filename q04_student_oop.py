"""Q4. OOP + Lists + Exception Handling."""


class Student:
    """Store student details and marks."""

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks_list = []

    def add_mark(self, mark):
        """Add a valid mark to the student marks list."""
        try:
            mark = float(mark)

            if mark < 0 or mark > 100:
                raise ValueError("Marks must be between 0 and 100.")

            self.marks_list.append(mark)
            print(f"Mark {mark} added successfully.")

        except ValueError as error:
            print(f"Invalid mark: {error}")

    def get_average(self):
        """Return average marks."""
        if not self.marks_list:
            return 0
        return sum(self.marks_list) / len(self.marks_list)

    def display_info(self):
        """Display student details."""
        print("\nStudent Details")
        print("-" * 30)
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_no}")
        print(f"Marks: {self.marks_list}")
        print(f"Average: {self.get_average():.2f}")


try:
    student_name = input("Enter student name: ").strip()
    student_roll = int(input("Enter roll number: "))
    student = Student(student_name, student_roll)

    total_marks = int(input("How many marks do you want to add? "))

    for count in range(1, total_marks + 1):
        mark_input = input(f"Enter mark {count}: ")
        student.add_mark(mark_input)

    student.display_info()

except ValueError:
    print("Invalid input. Roll number and total marks count must be numeric.")
