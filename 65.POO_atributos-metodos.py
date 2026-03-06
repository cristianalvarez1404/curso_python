
class Cuenta:
  total_cuentas = 0

  def __init__(self, usuario, saldo):
    self.usuario = usuario
    self.saldo = saldo
    Cuenta.total_cuentas += 1

  def depositar(self, valor):
    self.saldo += valor

  def retirar(self, valor):
    self.saldo -= valor

  def consultar_saldo(self):
    return f"Saldo de {self.usuario} es => {self.saldo}"
  

c1 = Cuenta("Ana",100)
c2 = Cuenta("Carlos",200)
c3 = Cuenta("Andres",500)

c1.depositar(200)
c1.retirar(50)
print(c1.consultar_saldo())
print(f"Total cuentas bancarias {Cuenta.total_cuentas}")