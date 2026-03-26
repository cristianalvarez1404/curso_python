class Usuario:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.__edad = edad

  @property
  def get_edad(self):
    print(self.__edad)

  @get_edad.setter
  def set_edad(self, nueva_edad):
    if nueva_edad > 0:
      self.__edad = nueva_edad
    else:
      print("Error en edad")

u1 = Usuario("Jhon",42)
u1.set_edad = -42
u1.get_edad