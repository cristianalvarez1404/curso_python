import unittest

class TestPedidos(unittest.TestCase):

  def test_unidades_pedido(self):
    unidades = 10
    self.assertGreaterEqual(unidades, 10)

  def test_total_pedido(self):
    cantidad = 10
    valor = 300
    total = cantidad * valor
    self.assertEqual(total, 3000)

  #@unittest.skip("Test pendiente por implementar")
  def test_descuento_pedido(self):
    descuento = 20
    self.assertEqual(descuento,20)

suit = unittest.TestSuite()
suit.addTest(TestPedidos("test_unidades_pedido"))
suit.addTest(TestPedidos("test_total_pedido"))
suit.addTest(TestPedidos("test_descuento_pedido"))

result = unittest.TestResult()
suit.run(result)

print("Test ejecutados: ", result.testsRun)
print("Fallos: ", result.failures)
print("Errores: ", result.errors)
print("Omitidos: ", result.skipped)

if result.wasSuccessful():
  print("TEST OK! ✅")
else:
  print("TEST CON ERRORES 😢")