# Comprensión de diccionarios

# numeros = {}

# for value in range(10):
#   numeros[value] = value * 2

numeros = { value:value *2 for value in range(10) if value % 2 }

print(numeros)