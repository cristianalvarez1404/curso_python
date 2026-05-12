
def validar(fn):
  def wrap(edad):
    if not isinstance(edad, int):
      print("La edad no es un numero")
      return
    
    if edad <= 0:
      print("La edad debe ser mayor a 0")
      return

    fn(edad) 
  return wrap

@validar
def registrar_usuario(edad):
  print(f"Usuario registrado con la edad {edad}")

registrar_usuario(-5)
registrar_usuario("hola")
registrar_usuario(47)