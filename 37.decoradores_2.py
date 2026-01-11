def decorador(fun):
  def wrapper():
    var1 = 10
    var2 = fun()
    return var1 * var2
  
  return wrapper

@decorador
def multiplicar():
  return 10

print(multiplicar())










# def decorador(fun):
#   def wrapper():
#     var = 50
#     var2 = fun()
#     return var + var2
#   return wrapper

# def numero_aleatorio():
#   return 10

# numero_aleatorio = decorador(numero_aleatorio)

# print(numero_aleatorio())