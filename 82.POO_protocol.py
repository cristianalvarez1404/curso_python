from typing import Protocol

class MetodoPago(Protocol):
  def pago(self, valor:float) -> None:
    ...

class PagoTransferencia:
  def pago(self, valor:float) -> None:
    print(f"Pago realizado por transferencia valor => ${valor}")

class PagoEfectivo:
  def pago(self, valor:float) -> None:
    print(f"Pago realizado en efectivo valor => ${valor}")

def procesar_pago(metodo:MetodoPago,valor:float):
  metodo.pago(valor)

m1 = PagoTransferencia()
m2 = PagoEfectivo()

procesar_pago(m1,1000)
procesar_pago(m2,2000)