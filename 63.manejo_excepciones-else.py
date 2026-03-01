
try:
  num = int(input("Digitar un número"))
except ValueError:
  print("Error en el número digitado")
else:
  print(f"numero digitado => {num}")
finally:
  print("Fin del programa")
  

try:
  num1 = int(input("Digitar número 1"))
  num2 = int(input("Digitar número 2"))
  resultado = num1 / num2
except ZeroDivisionError:
  print("No se puede dividir entre 0")
except ValueError:
  print("Error en el número digitado")
except Exception:
  print("Error en números")
else:
  print(f"El resultado de la división es => {resultado}")
finally:
  print("Fin del programa")