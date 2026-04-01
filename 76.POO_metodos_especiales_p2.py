
class Producto:
  def __init__(self, nombre, valor):
    self.nombre = nombre
    self.valor = valor

  def __add__(self, ob2):
    return self.valor + ob2.valor

  def __sub__(self, ob2):
    return self.valor - ob2.valor
  
  def __mul__(self, ob2):
    return self.valor * ob2.valor
  
  def __truediv__(self, ob2):
    return self.valor / ob2.valor
  
  def __eq__(self, obj):
    return self.valor == obj.valor
  
  def __gt__(self, obj):
    return self.valor > obj.valor
  
  def __lt__(self, obj):
    return self.valor < obj.valor

prod1 = Producto("Computador1",100)
prod2 = Producto("Computador2",300)

# print(prod1.nombre)
# print(prod1 + prod2)
# print(prod1 - prod2)
# print(prod1 * prod2)
# print(prod1 / prod2)
# print(prod1 == prod2)
# print(prod1 > prod2)
print(prod1 < prod2)