from abc import ABC, abstractmethod

class Canal:
  @abstractmethod
  def enviar(self, mensaje):
    pass

class Whatsapp(Canal):
  def enviar(self, mensaje):
    print(f"Canal de whatsapp : {mensaje}")

class Email(Canal):
  def enviar(self, mensaje):
    print(f"Canal de email : {mensaje}")


class Notificador:
  def __init__(self, canal:Canal):
    self.canal = canal

  @abstractmethod
  def enviar(self, message):
    pass

class NotificadorUrgente(Notificador):
  def enviar(self, message):
    self.canal.enviar(mensaje=message)

class NotificadorInformativo(Notificador):
  def enviar(self, message):
    self.canal.enviar(mensaje=message)

email = Email()
notificador = NotificadorInformativo(email)
notificador.enviar("Notificación informativa: ERROR del servidor")


# class NotificadorWhatsapp(Notificacion):
#   def enviar(self, mensaje):
#     print(f"Notificador por Whatapp: {mensaje}")

# class NotificadorEmail(Notificacion):
#   def enviar(self, mensaje):
#     print(f"Notificador por Email: {mensaje}")

# class NotificadorUrgenteWhatsapp(Notificacion):
#   def enviar(self, mensaje):
#     print(f"Notificador urgente por Whatapp: {mensaje}")

# class NotificadorUrgenteEmail(Notificacion):
#   def enviar(self, mensaje):
#     print(f"Notificador urgente por Email: {mensaje}")

# notificador = NotificadorUrgenteEmail()
# notificador.enviar("Servidor caido para pagos")