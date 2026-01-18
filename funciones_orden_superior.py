
# def sumar(valores):
#   sumatoria = 0
#   for i in valores:
#     sumatoria += i
#   return sumatoria

# def main(fun,*args):
#   return fun(args)

# print(main(sumar,1,2,3,5))

numeros = [2,4,6,8]

# resultado = list(map(lambda x : x * 2,numeros))
# print(resultado)
# resultado = list(filter(lambda x : x > 5, numeros))
# print(resultado)
resultado = max(numeros)
print(resultado)
# min()