"""Course class with name and grades."""


class Course:
    pass
from student import Student

class Course:
    def __init__(self, name: str):
        self.name = name
        self.grades = []

    def add_grade(self, student: Student, grade: int):
        self.grades.append((student, grade))

    def get_grades(self) -> list[tuple[Student, int]]:
        return self.grades

    def get_average_grade(self) -> float:
        if not self.grades:
            return -1
        return sum(grade for _, grade in self.grades) / len(self.grades)

    def __repr__(self):
        return self.name 