import Transcript
from student import Student
from advisor import print_alerts, scan_students, GPA_REQUIREMENT

def main():
    print("Driver code executed.")

    s1 = Student(
        name="Brandon Rachal",
        classification="Junior",
        major="Computer Science",
        enrolled_classes=["CPSC 2735", "CPSC 2120", "Math 2050"],
        minor="Business"
    )

    # Add grades
    s1.add_grade("CPSC 2735", "A")
    s1.add_grade("CPSC 2120", "B")
    s1.add_grade("Math 2050", "A")
    s1.calculate_gpa()

    s2 = Student(
        name="Chris Jackson",
        classification="Sophomore",
        major="Engineering",
        enrolled_classes=["ENGR 2010", "MATH 2070"]
    )
    s2.add_grade("ENGR 2010", "D")
    s2.add_grade("MATH 2070", "F")
    s2.calculate_gpa()

    students = [s1, s2]

    # Display info
    s1.display_info()

    # Check for minor
    print("Has a minor?", s1.has_minor())

    print(f"--- Advisor Alerts (threshold = {GPA_REQUIREMENT}) ---")
    below_count = print_alerts(students, threshold=GPA_REQUIREMENT)
    print(f"Total below threshold: {below_count}\n")

    # Option B: get messages as a list (for UI, logs, email, etc.)
    messages = scan_students(students, threshold=GPA_REQUIREMENT)

if __name__ == "__main__":
    main()