"""School class which stores information about courses and students."""


class School:
    pass
from student import Student
from course import Course

class School:
    def __init__(self, name: str):
        self.name = name
        self.students = []
        self.courses = []
        self.next_student_id = 1

    def add_course(self, course: Course):
        if course not in self.courses:
            self.courses.append(course)

    def add_student(self, student: Student):
        if student not in self.students:
            student.set_id(self.next_student_id)
            self.students.append(student)
            self.next_student_id += 1

    def add_student_grade(self, student: Student, course: Course, grade: int):
        if student in self.students and course in self.courses:
            student.add_grade(course, grade)
            course.add_grade(student, grade)

    def get_students(self) -> list[Student]:
        return self.students

    def get_courses(self) -> list[Course]:
        return self.courses

    def get_students_ordered_by_average_grade(self) -> list[Student]:
        return sorted(self.students, key=lambda s: s.get_average_grade(), reverse=True) 