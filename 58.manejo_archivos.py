archivo = open("contenido.txt", "r")
datos = archivo.read()
print(datos)
archivo.close()

with open("contenido.txt","r") as archivo:
  datos = archivo.read()
  print(datos)

with open("nuevo.txt", "w") as archivo:
  archivo.write("Hola desde el archivo main\n")
  archivo.write("y desde python\n")

with open("nuevo.txt", "a") as archivo:
  archivo.write("\nPracticando el manejo de archivos")