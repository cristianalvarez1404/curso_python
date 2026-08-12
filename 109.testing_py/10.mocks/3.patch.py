import unittest
from unittest.mock import patch
from calculadora import duplicar_valor

class Test_calculadora(unittest.TestCase):

  @patch("calculadora.obtener_valor")
  def test_duplicar_valor(self, mock_obtener_valor):
    mock_obtener_valor.return_value = 50
    num = duplicar_valor()

    self.assertEqual(num, 100)

if __name__ == "__main__":
  unittest.main()