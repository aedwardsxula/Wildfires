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

    def has_minor(self):
        """Return True if the student has a declared minor."""
        return self.minor is not None

    def add_grade(self, course, grade):
        """Add or update a grade for a course."""
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

    def display_info(self):
        """Display all student details."""
        print(f"Name: {self.name}")
        print(f"Classification: {self.classification}")
        print(f"Major: {self.major}")
        print(f"Minor: {self.minor if self.minor else 'None'}")
        print(f"GPA: {self.gpa}")
        print(f"Enrolled Classes: {', '.join(self.enrolled_classes)}")
        print(f"Grades: {self.grades}")