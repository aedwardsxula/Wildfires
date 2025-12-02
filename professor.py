class Professor:
    def __init__(self, name):
        self.name = name

    def enter_midterm_grade(self, student, grade):
        student.set_midterm_grade(grade)
        print(f"{self.name} entered midterm grade for {student.name}.")

    def enter_final_grade(self, student, grade):
        student.set_final_grade(grade)
        print(f"{self.name} entered final grade for {student.name}.")

    def view_transcript(self, student):
        print(student.get_transcript())
