import unittest

def calcular_descuento(valor, descuento):
  return valor - (valor * descuento / 100)

class TestDescuento(unittest.TestCase):
  def test_descuento(self):
    resultado = calcular_descuento(100, 33.33)
    self.assertAlmostEqual(resultado, 66.67, places=2)
    self.assertEqual(resultado, 66.67, places=2)

if __name__ == "__main__":
  unittest.main()