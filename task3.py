class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.is_enrolled = is_enrolled


class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)


# Creating Student objects
s1 = Student(101, "Maruf Billah", "Software Engineering", True)
s2 = Student(102, "Rahim Ahmed", "CSE", False)

# Manually inserting Student objects
StudentDatabase.add_student(s1)
StudentDatabase.add_student(s2)


# Displaying student information
for student in StudentDatabase.student_list:
    print(student.student_id, student.name,
        student.department, student.is_enrolled)