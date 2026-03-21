
class Persona:
  empresa = "Empresa ejemplo LTDA"

  def __init__(self,nombre):
    self.nombre = nombre

  def imprimir_nombre(self):
    print(f"Nombre de la persona: {self.nombre}")

  @classmethod
  def cambiar_compañia(cls,nueva_empresa):
    Persona.empresa = nueva_empresa

  @staticmethod
  def es_mayor_edad(edad):
    return edad >= 18
  

# p1 = Persona("Jhon")
# p2 = Persona("Sara")
# p1.imprimir_nombre()
# p2.imprimir_nombre()
# print(Persona.empresa)
Persona.cambiar_compañia("Otra empresas LTDA")
print(Persona.empresa)
print(Persona.es_mayor_edad(19))