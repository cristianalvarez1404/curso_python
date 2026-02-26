
try:
  num = 10 / 2
except ZeroDivisionError:
  print("Error en división")

try:
  num = 10 + "a"
except TypeError:
  print("Error en tipo de dato")

try:
  lista = ["a","b"]
  print(lista[2])
except IndexError:
  print("Error en el indice")

try:
  persona = {"nombre":"Joe"}
  print(persona["edad"])
except KeyError:
  print("Error en la key edad")

try:
  archivo = open("archivo.txt")
except FileNotFoundError:
  print("Error al leer el archivo")
except KeyError:
  print("Error en la key")
except IndexError:
  print("Error en el indice")
except Exception:
  print("Error general")

try:
  edad = int(input("Ingresar edad"))
  raise Exception("Error dentro del código")
except FileNotFoundError:
  print("Error al leer el archivo")
except KeyError:
  print("Error en la key")
except IndexError:
  print("Error en el indice")
except Exception as e:
  print(f"Error general {e}" )

try:
  num = 10 / 2
  raise Exception("Error en la base de datos")
except Exception as e:
  print(f"{e}")
finally:
  print("Desconexión de la base de datos")