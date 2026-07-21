import unittest

class TestCalculadora(unittest.TestCase):
  def test_esigual(self):
    valor = 5
    self.assertEqual(valor, 5)
  
  def test_isTrue(self):
    variable = True
    self.assertTrue(variable)

  def test_isFalse(self):
    variable = False
    self.assertFalse(variable)

  def test_isNone(self):
    usuario = None
    self.assertIsNone(usuario)

  def test_isIn(self):
    lista = ["red","verde","azul"]
    self.assertIn("azul", lista)

  def test_is(self):
    objetos = [1,2,3]
    lista = objetos
    self.assertIs(objetos, lista)

  def test_raise_Exception(self):
    def dividir(a, b):
      raise ZeroDivisionError("Error en division")
    
    with self.assertRaises(ZeroDivisionError):
      dividir(10,0)

if __name__ == "__main__":
  unittest.main()
