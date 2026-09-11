import unittest
from unittest.mock import patch, AsyncMock

async def consultar_servidor():
  return {
    "nombre":"Carlos",
    "edad": 42
  }

async def obtener_datos():
  resultado = await consultar_servidor()
  return resultado["nombre"]

class TestAPI(unittest.IsolatedAsyncioTestCase):

  @patch(__name__ + ".consultar_servidor", new_callable=AsyncMock)
  async def test_obtener_datos(self, mock_servidor):
    mock_servidor.return_value = {
      "nombre":"Carlos",
      "edad":42
    }

    resultado = await obtener_datos()

    self.assertEqual(resultado, "Carlos")

if __name__ == "__main__":
  unittest.main()