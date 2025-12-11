#List Comprehension - Comprensión de listas

lista1 = [1,2,3,4,5,6,7,8,9,10]

# lista2 = [ i * 2 if i >= 5 else "no se cumple" for i in lista1 ]
lista2 = [ i * 2 for i in lista1 if i > 20 ]

print(lista2)