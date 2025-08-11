
class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) == 10:
            raise ValueError('Max students reached!')
        self.group.add(student)


    def delete_student(self, last_name):
        to_remove = [s for s in self.group if s.last_name == last_name]
        for student in to_remove:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        if not self.group:
            return f'Number: {self.number}\n<No students>'
        all_students = " | ".join(str(s) for s in self.group)
        return f'Number: {self.number}\n{all_students}'

