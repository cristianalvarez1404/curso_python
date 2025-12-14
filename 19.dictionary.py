"key-value"

persona = {
  "nombre":"Joe",
  "apellido":"Doe",
  "edad":42,
  "direccion": [
    "CR 8",
    "Dg 9"
  ]
}

persona["trabaja"] = True
del persona["direccion"]
persona["edad"] = 48

print(persona)