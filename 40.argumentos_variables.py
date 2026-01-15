
def datos(*args, **kwargs):
  suma = sum(args)

  for key, value in kwargs.items():
    print(key, "-", value)

  print(suma)

datos(20,50,60,80,60,nombre="Joe",apellido="Doe",edad=52,direccion="CR 8")