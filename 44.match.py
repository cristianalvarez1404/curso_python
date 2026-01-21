
# option = 3

# if option == 1:
#   print("Ejecutando operacion 1")
# elif option == 2:
#   print("Ejecutando operacion 2")
# elif option == 3:
#   print("Ejecutando operacion 3")
# elif option == 4:
#   print("Ejecutando operacion 4")
# else:
#   print("Ejecutando operacion 5")


operacion = 2

match operacion:
  case 1:
    print("Operacion 1") 
  case 2:
    print("Operacion 2") 
  case 3:
    print("Operacion 3") 
  case 4:
    print("Operacion 4") 
  case _:
    print("Operacion 5") 



usuario = {"tipo_usuario":"otro"}

match usuario:
  case {"tipo_usuario":"admin","activo":False}:
    print("Usuario inactivo")
  case {"tipo_usuario":"admin","activo":True}:
    print("Usuario activo")

  case {"tipo_usario":"general"}:
    print("Usario general")

  case _:
    print("Usuario no reconocido")
  

edad = 16

match edad:
  case edad if edad >= 18:
    print("Mayor de edad")
  case _:
    print("Menor de edad")