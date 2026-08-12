import unittest
from unittest.mock import Mock

class Usuario:
  def buscar_usuario(self, base_datos):
    return base_datos.obtener_nombre(15)

class TestUsuario(unittest.TestCase):
  def test_usuario(self):
    base_datos = Mock()
    base_datos.obtener_nombre.return_value = "Carlos"

    usuario = Usuario()
    resultado = usuario.buscar_usuario(base_datos)
    resultado = usuario.buscar_usuario(base_datos)

    self.assertEqual(resultado, "Carlos")

    base_datos.obtener_nombre.assert_called()
    base_datos.obtener_nombre.assert_called_once()
    base_datos.obtener_nombre.assert_called_with(10)
    base_datos.obtener_nombre.assert_called_once_with(10)

if __name__ == "__main__":
  unittest.main()

