
# ternario en python
# match
# modulos
# f strings

cuentas_bancarias = []
nums_cuentas = 0

def crear_cuenta(datos_usuario):
  nueva_cuenta = datos_usuario
  nueva_cuenta["num_cuenta"] = nums_cuentas + 1

  if datos_usuario not in cuentas_bancarias:
    cuentas_bancarias.append(nueva_cuenta)
    print("Tu cuenta ha sido creada con éxito!")
    consultar_saldo(nueva_cuenta["num_cuenta"])
    return
  else:  
    print("Cuenta ya creada")
    return 

def depositar(cuenta_bancaria,valor):
  for cuenta in cuentas_bancarias:
    if cuenta["num_cuenta"] == cuenta_bancaria:
      cuenta["saldo"] = cuenta["saldo"] + valor
      print("Saldo depositado")
      consultar_saldo(cuenta_bancaria)
      break
    else:
      print("Cuenta no existe, por favor registrate")
      break
   

def retirar(cuenta_bancaria,valor):
   for cuenta in cuentas_bancarias:
    if cuenta["num_cuenta"] == cuenta_bancaria:
      saldo = cuenta["saldo"] = cuenta["saldo"]
      if saldo < valor:
        print("Fondos insuficientes")
      else:
        cuenta["saldo"] = cuenta["saldo"] - valor
      consultar_saldo(cuenta_bancaria)
      break
    else:
      print("Cuenta no existe, por favor registrate")
      break

def consultar_saldo(cuenta_bancaria):
  for cuenta in cuentas_bancarias:
    if cuenta["num_cuenta"] == cuenta_bancaria:
      
      print("Saldo de cuenta : ", cuenta["saldo"] )
      break
    else:
      print("Cuenta no existe, por favor registrate")
      break

def main():
  while True:
    option = int(input("""Selecciona una opcion: 
      1.Crear cuenta
      2.Depositar
      3.Retirar
      4.Consultar saldo
      5.Salir\n"""))
    
    if option == 1:
      print("Ingrese los siguiente datos : ")
      nombre = input("Nombre: ")
      edad = int(input("Edad: "))
      saldo = int(input("Saldo inicial: "))

      usuario = {
        "nombre": nombre,
        "edad": edad,
        "saldo": saldo or 0
      }
      crear_cuenta(usuario)
      break
    if option == 2:
      valor = int("Registre el valor a depositar: ")
      num_cuenta = int("Digite el número de cuenta: ")
      depositar(num_cuenta, valor)
      break
    if option == 3:
      valor = int("Registre el valor a retirar: ")
      num_cuenta = int("Digite el número de cuenta: ")
      retirar(num_cuenta,valor)
      break
    if option == 4:
      num_cuenta = int("Digite el número de cuenta: ")
      consultar_saldo(num_cuenta)
      break
    if option == 5:
      print("Adios!")
      break
  print("")

if __name__ == "__main__":
  main()