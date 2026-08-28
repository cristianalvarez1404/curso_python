import unittest
from usuario import es_mayor_de_edad

class TestUsuario(unittest.TestCase):
  def test_es_mayor_de_edad(self):
    self.assertTrue(es_mayor_de_edad(37))
