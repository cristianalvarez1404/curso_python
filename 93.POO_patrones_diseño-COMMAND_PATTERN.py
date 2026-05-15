
class Documento:
  def __init__(self):
    self.texto = ""
    self.alineacion = "izquierda"

  def escribir(self, texto):
    self.texto += texto

  def borrar(self, texto):
    self.texto = self.texto[:-len(texto)]

  def centrar(self):
    self.alineacion = "centrado"
    print("Texto centrado")

class EscribirCommand:
  def __init__(self, doc, texto):
    self.doc = doc
    self.texto = texto

  def ejecutar(self):
    self.doc.escribir(self.texto)

  def deshacer(self):
    self.doc.borrar(self.texto)


class CentrarCommand:
  def __init__(self,doc):
    self.doc = doc
    self.alineacion_anterior = "izquierda"

  def ejecutar(self):
    self.alineacion_anterior = self.doc.alineacion
    self.doc.centrar()

  def deshacer(self):
    self.doc.alineacion = self.alineacion_anterior


class Editor:
  def __init__(self):
    self.historial = []

  def ejecutar(self, command):
    command.ejecutar()
    self.historial.append(command)

  def deshacer(self):
    if self.historial:
      command = self.historial.pop()
      command.deshacer()


d = Documento()
editor = Editor()
editor.ejecutar(EscribirCommand(d,"hola "))
editor.ejecutar(EscribirCommand(d,"mundo"))
editor.ejecutar(CentrarCommand(d))
editor.deshacer()
editor.deshacer()
editor.deshacer()

print(d.alineacion)
print(d.texto)
