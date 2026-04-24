from abc import ABC,abstractmethod

class MetodoPago(ABC):
  @abstractmethod
  def pago(self, monto:float) -> None:
    pass

class Paypal(MetodoPago):
  def pago(self, monto:float) -> None:
    print(f"Pagando por paypal el valor de {monto}")

class Transferencia(MetodoPago):
  def pago(self, monto:float) -> None:
    print(f"Pagando por transferencia el valor de {monto}")

class FabricaPago:
  def crear_pago(self, tipo) -> MetodoPago:
    if tipo == 'paypal':
      return Paypal("usuario1","password")
    elif tipo == "transferencia":
      return Transferencia()
    else:
      raise ValueError("Error en método de pago")

def procesar_pago(tipo):
  fabrica = FabricaPago()
  metodo = fabrica.crear_pago(tipo)
  metodo.pago(2000)

procesar_pago("transferencia")



# def procesar_pago(tipo, monto):
#   if tipo == 'paypal':
#     metodo = Paypal("usuario1","password")
#   elif tipo == "transferencia":
#     metodo = Transferencia("usuario1","password")
#   else:
#     raise ValueError("Error en método de pago")


# procesar_pago("paypal",2000)