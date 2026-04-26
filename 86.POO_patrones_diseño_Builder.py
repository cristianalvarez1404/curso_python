
class Usuario:
  def __init__(self, nombre = None, apellido = None, edad = None, email = None, direccion = None, telefono = None):
    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad
    self.email = email
    self.direccion = direccion
    self.telefono = telefono

class UsuarioBuilder:
  def __init__(self):
    self.usuario = Usuario()

  def set_nombre(self,nombre ):
    self.usuario.nombre = nombre 
    return self
  
  def set_apellido(self,apellido):
    self.usuario.apellido = apellido 
    return self
  
  def set_edad(self,edad ):
    self.usuario.edad = edad 
    return self
  
  def set_email(self,email ):
    self.usuario.email = email 
    return self
  
  def set_direccion(self,direccion ):
    self.usuario.direccion = direccion 
    return self
  
  def set_telefono(self,telefono ):
    self.usuario.telefono = telefono 
    return self
  
  def build(self):
    return self.usuario


u1 = Usuario("Jhon","Doe",39,"email@gmail","CR 5", 12345)

u2 = UsuarioBuilder().set_nombre("Jhon").set_apellido("").set_edad(39).set_email("email@gmail.com").set_direccion("CR 5").set_telefono(12345).build()

print(u2.email)