import sys

print(sys.argv)

if len(sys.argv) < 3:
  sys.exit("Faltan argumentos: <name> <age>")

name = sys.argv[1]
age = sys.argv[2]

print(f"Hola {name} tienes {age} años.")

print(sys.platform)

sistema = sys.platform

if sistema == "win32":
  print("Ejecutanto en windows...")

elif sistema == "linux":
  print("Ejecutanto en linux...")

elif sistema == "darwin":
  print("Ejecutanto en Macos...")

print(sys.version)

if "3.13" in sys.version:
  print("Ejecutando programa...")
