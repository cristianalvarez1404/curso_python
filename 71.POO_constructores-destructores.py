
class Usuario:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  def __del__(self):
    print(f"Eliminando objeto y liberando memoria")


u1 = Usuario("Jhon",43)
# u2 = Usuario("Maria",32)
del u1

# print(u1.nombre)
# print(u1.edad)