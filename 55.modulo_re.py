import re

texto = "hola mund"
resultado = re.search("mundo", texto)

if not resultado:
  print("Palabra no encontrada")

password = "Hola111"
resultado = re.search("[a-z]+", password) # [a-z] +
resultado = re.search("[A-Z]+", password) # [A-Z] +
resultado = re.search("[a-zA-Z]+", password) # [A-Z] +
resultado = re.search("[0-9]+", password) # [0-9] +

texto = "Js Python ..."
resultado = re.search("^Python", texto) # ^ => Comienza por

texto = "archivo.py"
resultado = re.search(".txt$", texto) # $ => termina con 

texto = "hola hoooola la"
resultado = re.findall("ho*", texto) # * => cero o más veces

texto = "mundo mu?do mu_do"
resultado = re.findall("mu.do", texto) # . => cualquier caracter

texto = "Pedido 123 asddsdadsadsadds 54645564564564"
resultado = re.sub("[0-9]+","---", texto)

print(resultado)
