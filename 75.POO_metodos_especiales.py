
class Carrito:
  def __init__(self, producto, valor):
    self.producto = producto
    self.valor = valor

  def __str__(self):
    return f"{self.producto} - {self.valor}"
  
  def __repr__(self):
    return f"{self.producto} - {self.valor}"
  
  def __eq__(self, obj):
    return self.valor == obj.valor

  def __add__(self, obj):
    return self.valor + obj.valor

c1 = Carrito("Producto1",100)
c2 = Carrito("Producto2",100)

resultado = c1 + c2

print(resultado)