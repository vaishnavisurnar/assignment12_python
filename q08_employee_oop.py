"""Q8. Tuples + Dictionaries + OOP."""


class Employee:
    """Employee class with tuple details."""

    def __init__(self, emp_id, name, details):
        self.emp_id = emp_id
        self.name = name
        self.details = details

    def show_details(self):
        """Print employee information."""
        department, salary = self.details
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Department: {department}")
        print(f"Salary: {salary}")
        print("-" * 30)


employees = {
    101: Employee(101, "Aarav Patil", ("AI/ML", 45000)),
    102: Employee(102, "Vaishnavi Surnar", ("Data Science", 50000)),
    103: Employee(103, "Neha Sharma", ("Python Development", 48000)),
}

print("Employee Records")
print("=" * 30)

for employee in employees.values():
    employee.show_details()
