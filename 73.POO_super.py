
class Empleado:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  def info_empleado(self):
    print(f"Nombre del empleado => {self.nombre}")
    print(f"Edad del empleado => {self.edad}")

class Gerente(Empleado):
  def __init__(self,nombre, edad, area):
    super().__init__(nombre, edad)
    self.area = area

  def info_empleado(self):
    super().info_empleado()
    print(f"El área del gerente es: {self.area}")

e1 = Empleado("Jhon",43)
g1 = Gerente("Andres",38,"Administrativa")

g1.info_empleado()