import unittest
from unittest.mock import Mock

class Banco:
  def consultar_saldo(self):
    ...

class Cajero:
  def retirar(self, banco):
    return banco.consultar_saldo() > 1000

class TestCajero(unittest.TestCase):
  def test_retiro(self):
    banco = Mock()
    # banco.consultar_saldo.return_value = 5000
    banco.consultar_saldo.side_effect = [2000, 500]
    cajero = Cajero()
    self.assertTrue(cajero.retirar(banco))
    self.assertFalse(cajero.retirar(banco))

if __name__ == "__main__":
  unittest.main()