from typing import Iterable, List
from student import Student

GPA_REQUIREMENT = 2.0

def _ensure_gpa(student: Student) -> None:
    """
    If the student has grades but gpa isn't computed, compute it.
    Keeps things robust if caller forgot to call calculate_gpa().
    """
    if student.grades and (student.gpa is None or student.gpa == 0.0):
        student.calculate_gpa()

def student_below_gpa(student: Student, threshold: float = GPA_REQUIREMENT) -> bool:
    """Return True if student's GPA is below the threshold."""
    _ensure_gpa(student)
    return (student.gpa or 0.0) < threshold

def build_alert(student: Student, threshold: float = GPA_REQUIREMENT) -> str:
    """Return a formatted alert message for a single student (if below threshold)."""
    _ensure_gpa(student)
    if (student.gpa or 0.0) < threshold:
        return (
            f"⚠️ ALERT: {student.name} ({student.classification}) is below the GPA requirement "
            f"({student.gpa:.2f} < {threshold:.2f}).\n"
            f"Major: {student.major}  |  Minor: {student.minor or 'None'}\n"
            f"Enrolled: {', '.join(student.enrolled_classes)}\n"
            f"Advisor Action: Reach out and offer support.\n"
        )
    return f"✅ {student.name} meets GPA requirements ({student.gpa:.2f} ≥ {threshold:.2f})."

def scan_students(students: Iterable[Student], threshold: float = GPA_REQUIREMENT) -> List[str]:
    """
    Build alert messages for a list of students.
    Returns a list of strings (one message per student).
    """
    messages: List[str] = []
    for s in students:
        messages.append(build_alert(s, threshold))
    return messages

def print_alerts(students: Iterable[Student], threshold: float = GPA_REQUIREMENT) -> int:
    """
    Print alerts for all students and return the count of students BELOW the threshold.
    """
    count_below = 0
    for s in students:
        msg = build_alert(s, threshold)
        print(msg)
        if student_below_gpa(s, threshold):
            count_below += 1
    return count_below