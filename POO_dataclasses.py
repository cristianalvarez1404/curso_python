from dataclasses import dataclass

@dataclass
class Producto:
  nombre: str
  valor: int

p1 = Producto("Producto",100)
p2 = Producto("Producto",100)

print(p1 == p2)


class Producto:
  def __init__(self,nombre,valor):
    self.nombre = nombre
    self.valor = valor

  def __repr__(self):
    return f"Producto => {self.nombre} con valor {self.valor}"

  def __eq__(self,obj):
    return self.valor == obj.valor


p1 = Producto("Producto1",100)
p2 = Producto("Producto2",100)

print(p1.nombre)
print(p1.valor)
# print(p1 == p2)