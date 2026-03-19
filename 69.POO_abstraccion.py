from abc import ABC, abstractmethod

class Pago(ABC):
  @abstractmethod
  def metodo_pago(self):
    pass
  
  @abstractmethod
  def metodo_pago(self):
    pass

class PagoEfectivo(Pago):
  def metodo_pago(self):
    print("Pagado en efectivo...")

class PagoElectronico(Pago):
  def metodo_pago(self):
    print("Pago realizado electrónicamente...")

p1 = PagoEfectivo()
p2 = PagoElectronico()
lista_pagos = [p1,p2]

for pago in lista_pagos:
  pago.metodo_pago()