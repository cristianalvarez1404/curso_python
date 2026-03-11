
class Cuenta:
  def __init__(self, nombre, password, saldo):
    self.nombre = nombre
    self.__password = password
    self._saldo = saldo

  def cambiar_contraseña(self, nueva_contraseña, anterior_contraseña):
    if anterior_contraseña == self.__password:
      self.__password = nueva_contraseña
      print("Contrasela modificada")
    else:
      print("Error en contraseña")

  def imprimir_saldo(self):
    print(f"Su saldo es {self._saldo}")


c1 = Cuenta("Joe","Joe1",100)
c1.cambiar_contraseña("Joe11","Joe1")

# print(c1.nombre)
# print(c1.__password)
# print(c1._sa0ldo)
c1.imprimir_saldo()