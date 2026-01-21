
edad = 18

# if edad >= 18:
#   print("Mayor de edad")
# else:
#   print("Menor de edad")

print("Mayor de edad") if edad >= 18 else print("Menor de edad")

es_par = lambda a: print("Es par") if a % 2 == 0 else print("Es impar")

es_par(4)
es_par(7)
es_par(11)