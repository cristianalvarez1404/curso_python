
class Support1:
  def __init__(self, nextSupport = None):
    self.nextSupport = nextSupport

  def process(self, type):
    if type == "password":
      return "Soporte resulto por equipo 1"

    return self.nextSupport.process(type)

class Support2:
  def __init__(self, nextSupport = None):
    self.nextSupport = nextSupport

  def process(self, type):
    if type == "user":
      return "Soporte resulto por equipo 2"

    return self.nextSupport.process(type) 

class Enginner:
  def __init__(self, nextSupport = None):
    self.nextSupport = nextSupport

  def process(self, type):
    return "Soporte resulto por ingeniero senior"


support = Support1(Support2(Enginner()))

# print(support.process("password"))
# print(support.process("user"))
print(support.process("usuario eliminado"))