import csv

with open("datos1.csv","r") as archivo:
  contenido = csv.reader(archivo)

  for fila in contenido:
    print(fila[0])

with open("datos2.csv","r") as archivo:
  contenido = csv.reader(archivo,delimiter=";")

  for fila in contenido:
    print(fila)

with open("datos3.csv","w",newline="") as archivo:
  contenido = csv.writer(archivo)

  contenido.writerow(["nombre","edad","pais"])
  contenido.writerow(["Joe",42,"Mexico"])
  contenido.writerow(["Sara",31,"Peru"])

with open("datos1.csv","r") as archivo:
  contenido = csv.DictReader(archivo)

  for fila in contenido:
    print(f"Nombre => {fila["nombre"]} - edad => {fila["edad"]}")

with open("datos4.csv","w",newline="") as archivo:
  encabezados = ["nombre","edad","pais"]

  contenido = csv.DictWriter(archivo,fieldnames=encabezados)
  contenido.writeheader()

  contenido.writerow({"nombre":"Joe","edad":42,"pais":"Mexico"})
  contenido.writerow({"nombre":"Sara","edad":31,"pais":"Peru"})