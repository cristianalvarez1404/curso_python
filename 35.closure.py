x = 20

def funcion_padre():
  x = 10

  def funcion_hija():
    nonlocal x
    x += 5
    print(x)

  return funcion_hija

var1 = funcion_padre()

var1()