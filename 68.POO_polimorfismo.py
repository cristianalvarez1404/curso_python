
class Empleado:
  def __init__(self, nombre):
    self.nombre = nombre

  def calcular_salario(self):
    pass

class EmpleadoTiempoCompleto(Empleado):
  def calcular_salario(self):
    print(f"{self.nombre} gana 500 por mes")

class EmpleadoPorHora(Empleado):
  def calcular_salario(self):
    print(f"{self.nombre} gana 10 por hora")

e1 = EmpleadoTiempoCompleto("Sara")
e2 = EmpleadoPorHora("Joe")

empleados = [e1,e2]

for empleado in empleados:
  empleado.calcular_salario()