class Teacher:
  def __init__(self, name):
    self.name = name
    self.students = []

  def attach_students(self, student):
    self.students.append(student)
    print(f"{student.name} has been attached to {self.name}")

class Student:
  def __init__(self, name):
    self.teachers = []
    self.name = name

  def add_teachers(self, teacher):
    self.teachers.append(teacher)
    teacher.attach_students(self)


teacher_fzn = Teacher("FZN")
student_ryan = Student("Ryan")
student_ryan.add_teachers(teacher_fzn)