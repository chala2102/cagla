# Exercise 2: Student Grade Analyzer

# 1. Initialize Data Structures
student_grades = {}


# 2. Function to Add Student Grades
def add_student_grades(grades_db):
    name = input("Enter student name: ").strip()

    grades_input = input("Enter grades separated by spaces: ").strip()

    if not grades_input:
        print("No grades entered.")
        return

    try:
        grades = [float(grade) for grade in grades_input.split()]
    except ValueError:
        print("Invalid grade entered. Please use numbers only.")
        return

    if name in grades_db:
        grades_db[name].extend(grades)
        print(f"Grades added for existing student {name}.")
    else:
        grades_db[name] = grades
        print(f"Student {name} added.")


# 3. Function to Calculate Statistics
def get_student_stats(grades_db, student_name):

    if student_name not in grades_db:
        print("Student not found.")
        return

    grades = grades_db[student_name]

    if not grades:
        print("No grades available.")
        return

    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)

    print(f"\nStatistics for {student_name}")
    print(f"Grades: {grades}")
    print(f"Average: {average:.2f}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")


# 4. Function to Generate Full Report
def generate_full_report(grades_db):

    if not grades_db:
        print("No student data available.")
        return

    total_sum = 0
    total_count = 0

    print("\nFull Report")
    print("-" * 30)

    for name, grades in grades_db.items():

        if grades:
            average = sum(grades) / len(grades)
            highest = max(grades)
            lowest = min(grades)

            total_sum += sum(grades)
            total_count += len(grades)

        else:
            average = highest = lowest = 0

        print(f"\nName: {name}")
        print(f"Grades: {grades}")
        print(f"Average: {average:.2f}")
        print(f"Highest: {highest}")
        print(f"Lowest: {lowest}")

    if total_count > 0:
        overall_average = total_sum / total_count
        print("\nOverall Average Grade:", f"{overall_average:.2f}")


# 5. Main Program Loop
while True:

    print("\nStudent Grade Analyzer Menu:")
    print("1. Add grades for a student")
    print("2. View statistics for a student")
    print("3. Generate full report")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student_grades(student_grades)

    elif choice == '2':
        name = input("Enter student name: ")
        get_student_stats(student_grades, name)

    elif choice == '3':
        generate_full_report(student_grades)

    elif choice == '4':
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")