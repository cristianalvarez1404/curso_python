import random

print(random.random())
print(random.randint(1,20))

lista = ["Manzanas","Peras","Mandarinas"]

random.shuffle(lista)
print(lista)

numeros = [1, 2 ,3 , 4 ,5]

print(random.choice(numeros))
print(random.choices(numeros))
print(random.uniform(1, 10))