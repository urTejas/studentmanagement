# student_manager.py

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def to_dict(self):
        return {"Name": self.name, "Age": self.age, "Course": self.course}


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_all_students(self):
        return [student.to_dict() for student in self.students]

    def search_student(self, name):
        return [student.to_dict() for student in self.students if name.lower() in student.name.lower()]
