class StudentDatabase:
    stdnt_list = []

    @classmethod
    def add_student(cls, student):
        cls.stdnt_list.append(student)