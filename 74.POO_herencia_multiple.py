class Estudiante:
  def accion(self):
    print("Estudiando...")

class Trabajador:
  def accion(self):
    print("Trabajando...")

class Persona(Estudiante,Trabajador):
  def accion(self):
    print("Haciendo ejercicio...")

p1 = Persona()
print(Persona.__mro__)