"""Q5. Dictionaries + Functions + Control Structures."""


def student_database():
    """Menu-based student database using dictionary."""
    students = {}

    while True:
        print("\nStudent Database Menu")
        print("1. Add Student")
        print("2. Search Student by Roll Number")
        print("3. Display All Students")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                roll_no = int(input("Enter roll number: "))
                name = input("Enter name: ").strip()
                age = int(input("Enter age: "))
                city = input("Enter city: ").strip()

                students.update(
                    {
                        roll_no: {
                            "name": name,
                            "age": age,
                            "city": city,
                        }
                    }
                )
                print("Student added successfully.")

            except ValueError:
                print("Invalid input. Roll number and age must be numeric.")

        elif choice == "2":
            try:
                roll_no = int(input("Enter roll number to search: "))
                student = students.get(roll_no)

                if student:
                    print(f"Roll Number: {roll_no}")
                    print(f"Name: {student['name']}")
                    print(f"Age: {student['age']}")
                    print(f"City: {student['city']}")
                else:
                    print("Student not found.")

            except ValueError:
                print("Invalid roll number.")

        elif choice == "3":
            if not students:
                print("No student records available.")
            else:
                print("\nAll Student Records")
                for roll_no, student in students.items():
                    print(f"{roll_no}: {student}")

        elif choice == "4":
            print("Exiting student database.")
            break

        else:
            print("Invalid choice. Please select 1 to 4.")


student_database()
