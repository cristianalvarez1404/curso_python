"""
| ----------------------------------- | -------------------------------------- |
| **Single Responsibility Principle** | Principio de Responsabilidad unica     |
| **Open/Closed Principle**           | Principio Abierto/Cerrado              |
| **Liskov Substitution Principle**   | Principio de Sustitucion de Liskov     |
| **Interface Segregation Principle** | Principio de Segregacion de Interfaces |
| **Dependency Inversion Principle**  | Principio de Inversion de Dependencias |
"""

class Usuario:
  def guadar_usuario(self):
    print("Guardando usuario...")

class EmailService:
  def enviarEmail(self, texto):
    print("Enviando email...")

class Inventario:
  def registrando_compra(self, productos):
    print("Registrando productos...")

#--------------------------------------
from abc import ABC, abstractmethod

class AplicarDescuento(ABC):
  @abstractmethod
  def aplicar_descuento(self, tipo, valor):
    pass

# class Descuento(AplicarDescuento):
#   def aplicar_descuento(self, tipo, valor):
#     if tipo == 'vip':
#       return valor * 0.5
#     elif tipo == "compras":
#       return valor * 0.7
#     else:
#       return valor * 0.8
    
class DescuentoNormal(AplicarDescuento):
  def aplicar_descuento(self, tipo, valor):
    return valor * 0.8
  
class DescuentoVIP(AplicarDescuento):
  def aplicar_descuento(self, tipo, valor):
    return valor * 0.5
  
class DescuentoEspecial(AplicarDescuento):
  def aplicar_descuento(self, tipo, valor):
    return valor * 0.7

#------------------------------------------------

class Vehiculo(ABC):
  pass

class VehiculoMotor(Vehiculo):
  def encender(self):
    print("Encendiendo....")

class Moto(VehiculoMotor):
  pass

class Bicicleta(Vehiculo):
  pass

#-------------------------------------------------
class PersonalAseo:
  def limpiar_oficina(self):
    print("Limpiando...")

class PersonalInformatica:
  def programar(self):
    print("Programando...")

class PersonalRecursosHumanos:
  def seleccionar_personal(self):
    print("Seleccionando personal...")

class Programador(PersonalInformatica):
  pass

#------------------------------------------
class BaseDatos(ABC):
  @abstractmethod
  def guardar_datos(self, datos):
    pass

class MySQL(BaseDatos):
  def guardar_datos(self, datos):
    print("Guardando datos....")

class PostgreSQL(BaseDatos):
  def guardar_datos(self, datos):
    print("Guardando datos....")

class UsuarioService:
  def __init__(self, base_datos:BaseDatos):
    self.db = base_datos()

mysql = MySQL()
postgresql = PostgreSQL()

usuario = UsuarioService(mysql)
usuario = UsuarioService(postgresql)


