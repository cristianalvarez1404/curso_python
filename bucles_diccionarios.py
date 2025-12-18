producto = {
  "nombre" : "producto 1",
  "precio" : 100,
  "colores" : ["azul","rojo"],
  "disponible": True 
}

carrito = {
  "producto1" : 100,
  "producto2" : 200,
  "producto3" : 300,
}

total_factura = 0

for key,value in carrito.items():
  total_factura += value 

print(total_factura)


# for key,value in producto.items():
#   if key == "precio" and value > 50 :
#     print("El diccionario contiene la propiedad precio superior a 50")
#   else:
#     print("Dato no valido")

# for prop in producto:
#   print(prop)   

# for prop in producto.keys():
#   print(prop)   

# for values in producto.values():
#   print(values)

# for key,value in producto.items():
#   print(key,"-----",value)
