import unittest

class Calculadora:
  def sumar(self, a , b):
    return a + b
  
  def restar(self, a , b):
    return a - b

  def multiplicar(self, a , b):
    return a * b

  def dividir(self, a , b):
    return a / b

class TestCalculadora(unittest.TestCase):

    def setUp(self):
      self.calculadora = Calculadora()

    def test_suma(self):
      self.assertEqual(self.calculadora.sumar(10,5),15)

    def test_resta(self):
      self.assertEqual(self.calculadora.restar(10,5),5)

    def test_multiplicacion(self):
      self.assertEqual(self.calculadora.multiplicar(10,5),50)

    def test_division(self):
      self.assertEqual(self.calculadora.dividir(10,5), 2)

suite = unittest.TestSuite()
suite.addTest(TestCalculadora("test_suma"))
suite.addTest(TestCalculadora("test_multiplicacion"))
suite.addTest(TestCalculadora("test_resta"))

runner = unittest.TextTestRunner()
runner.run(suite)