import asyncio
import unittest

async def obtener_datos():
  await asyncio.sleep(3)
  return "Datos cargados"

# resultado = asyncio.run(obtener_datos())
# print(resultado)

class TestDB(unittest.IsolatedAsyncioTestCase):
  async def test_obtener_datos(self):
    resultado = await obtener_datos()
    self.assertEqual(resultado, "Datos cargados")

if __name__ == "__main__":
  unittest.main()