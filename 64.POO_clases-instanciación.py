
class Product:
  def __init__(self,nombre,color,cantidad):
    self.nombre = nombre
    self.color = color
    self.cantidad = cantidad

  def retirar_inventario(self, cantidad):
    self.cantidad -= cantidad
    print(f"Cantidad en inventario {self.cantidad}")

class Usuario:
  def __init__(self,nombre,email):
    self.nombre = nombre
    self.email = email

  def imprimir_nombre(self):
    print(f"Tu nombre es {self.nombre}")

p100 = Product("Producto100","Rojo",5)
p200 = Product("Producto200","Azul",10)
u1 = Usuario("Usuario1","usuario1@gmail.com")
u2 = Usuario("Usuario2","usuario2@gmail.com")

print(p100.cantidad)
print(u1.email)
print(u2.nombre)

p200.retirar_inventario(2)