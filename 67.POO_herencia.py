
class Usuario:
  def __init__(self, nombre):
    self.nombre = nombre

  def usuario_registrado(self):
    print(f"Usario {self.nombre} esta registrado.")

class Admin(Usuario):
  def usuario_registrado(self):
    print(f"Usuario registrado.")

  def eliminar_usuario(self):
    print("Eliminando usuario...")


u1 = Usuario("Joe")
a1 = Admin("Andres")

# u1.usuario_registrado()
a1.usuario_registrado()
a1.eliminar_usuario()