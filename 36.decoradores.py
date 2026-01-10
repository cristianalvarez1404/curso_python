def numero():
  return 5

def envolvente(fun_numero):
  def suma():
    var1 = 10
    var2 = fun_numero()
    return var1 + var2

  return suma

var3 = envolvente(numero)

print(var3())