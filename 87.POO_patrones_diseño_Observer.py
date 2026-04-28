from abc import ABC, abstractmethod

class Observer(ABC):
  @abstractmethod
  def actualizar(self, datos:dict):
    pass

class EmailService(Observer):
  def actualizar(self, datos):
    print(f"Enviando email por un valor de ${datos["valor"]}")

class InventarioService(Observer):
  def actualizar(self, datos):
    print(f"Actualizando invenatior...")

class AnaliticasService(Observer):
  def actualizar(self, datos):
    print(f"Actualizando analiticas...")

class Usuario(Observer):
  def actualizar(self, datos):
    print(f"Actualizando usuario sección compras...")

class ProcesarPagos:
  def __init__(self):
    self.observers = []

  def registrar_observer(self, observer:Observer):
    self.observers.append(observer)

  def remover_observer(self, observer:Observer):
    self.observers.remove(observer)

  def notificar_observadores(self, datos:dict):
    for o in self.observers:
      o.actualizar(datos)

  def procesar(self, datos):
    print(f"Pago procesado por valor de ${datos["valor"]}")
    self.notificar_observadores(datos)

procesador_pagos = ProcesarPagos()
procesador_pagos.registrar_observer(EmailService())
procesador_pagos.registrar_observer(InventarioService())
procesador_pagos.registrar_observer(AnaliticasService())
procesador_pagos.registrar_observer(Usuario())
procesador_pagos.remover_observer(Usuario())

procesador_pagos.procesar({"productos":["producto1","producto2"],"valor":2000})



# class ProcesarPago:
#   def procesar(self, valor):
#     print(f"Pago procesado por un valor de ${valor}")
#     self.enviar_email(valor)
#     self.actualizar_inventario(valor)
#     self.actualizar_analiticas(valor)

#   def enviar_email(self, valor):
#     print(f"Enviando email por compra de ${valor}")
  
#   def actualizar_inventario(self, valor):
#     print(f"Actualizando inventario...")

#   def actualizar_analiticas(self, valor):
#     print(f"Actualizando analiticas...")

    
# pago = ProcesarPago()
# pago.procesar(2000)