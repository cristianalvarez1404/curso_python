
class Graficos:
  def validar_graficos(self):
    print("Validando graficos...")

class RAM:
  def validar_ram(self):
    print("Validando memeoria...")

class Red:
  def validar_red(self):
    print("Validando red...")


class Validador:
  def __init__(self, graficos,ram,red):
    self.graficos = graficos
    self.ram = ram
    self.red = red

  def validar_recursos(self):
    self.graficos.validar_graficos()
    self.ram.validar_ram()
    self.red.validar_red()


graficos = Graficos()
ram = RAM()
red = Red()

validador = Validador(graficos,ram,red)
validador.validar_recursos()

