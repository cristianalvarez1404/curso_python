#JSON - JavaScript Object Notation
import json

datos = {
  "nombre":"Joe",
  "edad":47,
  "tiene_mascotas":False
}

convetir_JSON = json.dumps(datos)
# print(convetir_JSON)

datos2 = '{"nombre": "Joe", "edad": 47, "tiene_mascotas": false}'

convertir_py = json.loads(datos2)

print(convertir_py["edad"])