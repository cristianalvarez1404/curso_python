from abc import ABC, abstractmethod

class Estado(ABC):
  @abstractmethod
  def avanzar(self, pedido):
    pass

class Pagar(Estado):
  def avanzar(self, pedido):
    print("Pagando producto")
    pedido.estado = Enviar()

class Enviar(Estado):
  def avanzar(self, pedido):
    print("Enviando producto")
    pedido.estado = Entregar()

class Entregar(Estado):
  def avanzar(self, pedido):
    print("Producto entregado")

class Pedido:
  def __init__(self):
    self.estado = Pagar()

  def proceso_siguiente(self):
    self.estado.avanzar(self)

pedido = Pedido()
pedido.proceso_siguiente()
pedido.proceso_siguiente()
pedido.proceso_siguiente()


# class Pedido:
#   def __init__(self):
#     self.estado = "pendiente"

#   def avanzar(self):
#     if self.estado == "pendiente":
#       print("Pagando producto...")
#       self.estado = "pagado"
    
#     elif self.estado == "pagado":
#       print("Enviando producto...")
#       self.estado = "enviado"
    
#     elif self.estado == "enviado":
#       print("producto entregado")
#       self.estado = "entregado"

# pedido = Pedido()
# pedido.avanzar()
# pedido.avanzar()
# pedido.avanzar()