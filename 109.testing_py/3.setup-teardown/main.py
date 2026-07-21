import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

  def setUp(self):
    print("Conectando base de datos SQL...")
    self.calc = Calculadora()

  def tearDown(self):
    print("Cerrando base de datos...")

  def test_sumar(self):
    result = self.calc.sumar(5,3)
    self.assertEqual(result, 8)

  def test_resta(self):
    result = self.calc.restar(5,3)
    self.assertEqual(result, 2)

if __name__ == "__main__":
  unittest.main()