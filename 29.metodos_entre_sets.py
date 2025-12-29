a = {1, 2, 3 }
b = {4, 5, 6, 3,2}

resultado = a.union(b)
resultado1 = a | b

resultado = a.intersection(b)
resultado1 = a & b

resultado = a - b
resultado1 = b - a
resultado2 = a.difference(b)

resultado = a.symmetric_difference(b)
resultado1 = a ^ b

print(resultado1)