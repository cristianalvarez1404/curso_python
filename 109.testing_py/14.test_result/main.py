import unittest

class TestPedidos(unittest.TestCase):

  def test_unidades_pedido(self):
    unidades = 10
    self.assertGreaterEqual(unidades, 10)

  def test_total_pedido(self):
    cantidad = 3
    valor = 100
    total = cantidad * valor
    self.assertEqual(total, 300)

  @unittest.skip("Test pendiente de implementar...")
  def test_descuento_pedido(self):
    descuento = 20
    self.assertEqual(descuento,20)

suite = unittest.TestSuite()
suite.addTest(TestPedidos("test_unidades_pedido"))
suite.addTest(TestPedidos("test_total_pedido"))
suite.addTest(TestPedidos("test_descuento_pedido"))

result = unittest.TestResult()
suite.run(result)

print("Tests ejecutados: ", result.testsRun)
print("Fallos: ", result.failures)
print("Error: ", result.errors)
print("Omitidos: ", result.skipped)

if result.wasSuccessful():
  print("Test Ok! ✅")
else:
  print("Test con errores 😢")
