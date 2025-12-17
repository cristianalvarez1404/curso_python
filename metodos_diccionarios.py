persona = {
  "nombre":"Joe",
  "edad":45,
  "direcciones": [
    "CR 80",
    "DG 9"
  ],
  "pasatiempos": [
    "leer",
    "escuchar música"
  ],
  "tiene_licencia":False,
  "hermanos":4
}

# persona2 = persona.copy()
# del persona["hermanos"]
# print(persona.get("edad"))
# print(persona.pop("hermanos"))
# print(persona.popitem())
# persona.clear()
# persona.setdefault("hermanos",2)
persona.update({
  "musica_favorita":"Rock",
  "color_favorito":"Azul"
})

print(persona)
