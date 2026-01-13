def persona(**kwargs):
  print(kwargs["nombre"])
  print(kwargs.get("direccion"))

persona(nombre="Joe",apellido="Doe",edad=42,direccion="Cr 45")