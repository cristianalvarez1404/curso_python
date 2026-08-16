import unittest
from unittest.mock import patch

class Banco:
  def consultar_saldo(self):
    return 5000

class TestBanco(unittest.TestCase):
  def test_saldo(self):
    banco = Banco()

    with patch.object(Banco, "consultar_saldo") as Mock_saldo:
      Mock_saldo.return_value = 2000

      self.assertEqual(banco.consultar_saldo(), 2000)

if __name__ == "__main__":
  unittest.main()