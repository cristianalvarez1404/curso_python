import unittest
from verificacion_mocks import sumar, restar, multiplicar, dividir

class TestCalculadora(unittest.TestCase):
  def test_sumar(self):
    resultado = sumar(5,5)
    self.assertEqual(resultado, 10)
  
  def test_resta(self):
    resultado = restar(6,2)
    self.assertEqual(resultado, 4)
  
  def test_multiplicacion(self):
    resultado = multiplicar(2,2)
    self.assertEqual(resultado, 4)

  def test_division(self):
    resultado = dividir(6,2)
    self.assertEqual(resultado,3)

  def metodo_aux(self):
    pass


if __name__ == "__main__":
  unittest.main()