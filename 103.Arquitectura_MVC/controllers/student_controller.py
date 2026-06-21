from views.student_view import StudentView
from models.student import Student

class StudentController:
  def __init__(self):
    self.view = StudentView()

  def create_student(self, name, grade):
    if grade < 0 or grade > 100:
      self.view.print_info("Error en la calificación > 0")
      return
    
    student = Student(name, grade)

    if grade > 60:
      status = "Aprobo"
    else:
      status = "Reprobo"

    self.view.print_student(student)
    self.view.print_info(status)



