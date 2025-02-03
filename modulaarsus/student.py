"""Student class with student name and grades."""


class Student:
    pass
from course import Course

class Student:
    def __init__(self, name: str):
        self.name = name
        self.id = None
        self.grades = {}

    def set_id(self, id: int):
        if self.id is None:
            self.id = id

    def get_id(self) -> int:
        return self.id

    def add_grade(self, course: Course, grade: int):
        self.grades[course] = grade

    def get_grades(self) -> list[tuple[Course, int]]:
        return list(self.grades.items())

    def get_average_grade(self) -> float:
        if not self.grades:
            return -1
        return sum(self.grades.values()) / len(self.grades)

    def __repr__(self) -> str:
        return self.name 