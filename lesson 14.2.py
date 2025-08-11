class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name} age={self.age} gender={self.gender}"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str} record_book={self.record_book}"

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return str(self) == str(other)

    def __hash__(self):
        # Consistent with __eq__
        return hash(str(self))


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


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Male', 25, 'John', 'Jobs3', 'AN145')
st3 = Student('Female', 25, 'Liza', 'Taylor3', 'AN146')
st4 = Student('Female', 25, 'Liza', 'Taylor4', 'AN147')
st5 = Student('Female', 25, 'Liza', 'Taylor5', 'AN148')
st6 = Student('Female', 25, 'Liza', 'Taylor6', 'AN149')
st7 = Student('Female', 25, 'Liza', 'Taylor7', 'AN150')
st8 = Student('Female', 25, 'Liza', 'Taylor8', 'AN151')
st9 = Student('Female', 25, 'Liza', 'Taylor9', 'AN152')
st10 = Student('Female', 25, 'Liza', 'Taylor10', 'AN152')
st11 = Student('Female', 25, 'Liza', 'Taylor11', 'AN153')

gr = Group('PD1')

try:
    gr.add_student(st1)
except ValueError as e:
    print(f"Error: {e}")

try:
    gr.add_student(st2)
except ValueError as e:
    print(f"Error: {e}")

try:
    gr.add_student(st3)
except ValueError as e:
    print(f"Error: {e}")

try:
    gr.add_student(st4)
except ValueError as e:
    print(f"Error: {e}")

try:
    gr.add_student(st5)
except ValueError as e:
    print(f"Error: {e}")

try:
    gr.add_student(st6)
except ValueError as e:
    print(f"Error: {e}")

try:
    gr.add_student(st7)
except ValueError as e:
    print(f"Error: {e}")

try:
    gr.add_student(st8)
except ValueError as e:
    print(f"Error: {e}")

try:
    gr.add_student(st9)
except ValueError as e:
    print(f"Error: {e}")

try:
    gr.add_student(st10)
except ValueError as e:
    print(f"Error: {e}")

try:
    gr.add_student(st11)
except ValueError as e:
    print(f"Error: {e}")

print(gr)


assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
assert gr.find_student('Jobs2') is None

gr.delete_student('Taylor')
print(gr) # Only one student
