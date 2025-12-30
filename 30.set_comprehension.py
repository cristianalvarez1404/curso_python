#compresión de sets

lista = [1,2,3,4,5,5]

sets = { i * 2 for i in lista }

sets2 = { i * 2 for i in lista if i > 3}

print(sets2)