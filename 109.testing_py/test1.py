import unittest

class TestUsuario(unittest.TestCase):

  def test_assert_equal(self):
    resultado = 2 + 3
    self.assertEqual(resultado, 5)

  def test_usuario_activo(self):
    activo = True
    self.assertTrue(activo)
  
  def test_usuario_bloqueado(self):
    bloqueado = False
    self.assertFalse(bloqueado)

  def test_assert_is(self):
    lista = [1,2,3]
    otra_lista = lista

    self.assertIs(lista, otra_lista)
  
  def test_isNone(self):
    variable = None

    self.assertIsNone(variable)
  
  def test_isIn(self):
    colores = ["rojo","verde","azul"]

    self.assertIn("azul", colores)
  
  def test_isInstance(self):
    numero = 10

    self.assertIsInstance(numero, int)

  def test_raiseException(self):
    def dividir(a,b):
      raise ZeroDivisionError("Error")

    with self.assertRaises(ZeroDivisionError):
      dividir(10,0)


if __name__ == "__main__":
  unittest.main()

