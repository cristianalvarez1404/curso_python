from abc import ABC, abstractmethod

class DescuentoStrategy(ABC):
  @abstractmethod
  def procesar(self, valor):
    pass

class EmpleadoDescuento(DescuentoStrategy):
  def procesar(self, valor):
    print(f"Descuento para empleado => ${valor * 0.8}")

class VipDescuento(DescuentoStrategy):
  def procesar(self, valor):
    print(f"Descuento para vip => ${valor * 0.6}")

class EventoDescuento(DescuentoStrategy):
  def procesar(self, valor):
    print(f"Descuento para evento => ${valor * 0.5}")
    
class SinDescuento(DescuentoStrategy):
  def procesar(self, valor):
    print(f"Sin descuento => ${valor}")

class ProcesarDescuento:
  def __init__(self, strategy:DescuentoStrategy):
    self.strategy = strategy

  def procesar_pago(self, valor):
    self.strategy.procesar(valor)

pago = ProcesarDescuento(VipDescuento())
pago = ProcesarDescuento(EventoDescuento())
pago.procesar_pago(2000)

  

# class ProcesarDescuento:
#   def procesar(self, tipo, valor):
#     if tipo == "empleado":
#       print(f"Descuento para empleado => ${valor * 0.8}")
#     elif tipo == "vip":
#       print(f"Descuento para vip => ${valor * 0.6}")
#     elif tipo == "evento":
#       print(f"Descuento para evento => ${valor * 0.5}")
#     else:
#       print(f"Sin descuento => ${valor}")

# pago = ProcesarDescuento()
# pago.procesar("vip",1000)