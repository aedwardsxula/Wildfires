import Transcript
from student import Student

def main():
    print("Driver code executed.")

    student1 = Student(
        name="Brandon Rachal",
        classification="Junior",
        major="Computer Science",
        enrolled_classes=["CPSC 2735", "CPSC 2120", "Math 2050"],
        minor="Business"
    )

    # Add grades
    student1.add_grade("CPSC 2735", "A")
    student1.add_grade("CPSC 2120", "B")
    student1.add_grade("Math 2050", "A")

    # Calculate GPA
    student1.calculate_gpa()

    # Display info
    student1.display_info()

    # Check for minor
    print("Has a minor?", student1.has_minor())

if __name__ == "__main__":
    main()