class Student:
    def __init__(self, name, classification, major, enrolled_classes, gpa=0.0, grades=None, minor=None):
        """
        Initialize a new Student object.
        """
        self.name = name
        self.classification = classification
        self.major = major
        self.minor = minor
        self.enrolled_classes = enrolled_classes
        self.gpa = gpa
        self.grades = grades if grades is not None else {}

        # NEW attributes for midterm and final grades
        self.midterm_grade = None
        self.final_grade = None

    def has_minor(self):
        """Return True if the student has a declared minor."""
        return self.minor is not None

    def add_grade(self, course, grade):
        """Add or update a grade for a course (letter grades)."""
        self.grades[course] = grade

    def calculate_gpa(self):
        """Calculate GPA based on letter grades."""
        if not self.grades:
            return 0.0

        grade_points = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
        total_points = 0
        for grade in self.grades.values():
            total_points += grade_points.get(grade.upper(), 0)

        self.gpa = round(total_points / len(self.grades), 2)
        return self.gpa

    # ---------- NEW METHODS ----------
    def set_midterm_grade(self, grade):
        """Set the student's midterm grade."""
        self.midterm_grade = grade

    def set_final_grade(self, grade):
        """Set the student's final grade."""
        self.final_grade = grade

    def get_transcript(self):
        """Return a formatted transcript for the student."""
        return (
            f"--- Transcript ---\n"
            f"Name: {self.name}\n"
            f"Classification: {self.classification}\n"
            f"Major: {self.major}\n"
            f"Minor: {self.minor if self.minor else 'None'}\n"
            f"GPA: {self.gpa}\n"
            f"Enrolled Classes: {', '.join(self.enrolled_classes)}\n"
            f"Letter Grades: {self.grades}\n"
            f"Midterm Grade: {self.midterm_grade}\n"
            f"Final Grade: {self.final_grade}\n"
        )

    # -------------------------------

    def display_info(self):
        """Display all student details."""
        print(f"Name: {self.name}")
        print(f"Classification: {self.classification}")
        print(f"Major: {self.major}")
        print(f"Minor: {self.minor if self.minor else 'None'}")
        print(f"GPA: {self.gpa}")
        print(f"Enrolled Classes: {', '.join(self.enrolled_classes)}")
        print(f"Grades: {self.grades}")
        print(f"Midterm Grade: {self.midterm_grade}")
        print(f"Final Grade: {self.final_grade}")
