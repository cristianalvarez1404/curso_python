import unittest

class Banco:
  def retirar(self, saldo, valor):
    if valor > saldo:
      raise ValueError("Saldo insuficiente")

    return saldo - valor

class TestBanco(unittest.TestCase):
  def test_retiro(self):
    banco = Banco()

    with self.assertRaises(ValueError) as context:
      banco.retirar(1000,1500)

    self.assertEqual(str(context.exception), "Saldo insuficiente")

if __name__ == "__main__":
  unittest.main()