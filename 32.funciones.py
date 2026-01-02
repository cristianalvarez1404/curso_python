
num1 = 6
num2 = 8

def total_ventas():
  if num1 > num2:
    return num1 + num2
  else:
    print("El numero 1 no es mayor al numero 2")


def imprimir_nombre(nombre="Sin nombre", edad = 18):
  # if edad > 18:
  #   print("")
  
  # print("Hola " + nombre + " tienes " + str(edad) + "años")
  return edad

var3 = imprimir_nombre("Joe", 47)
print(var3)