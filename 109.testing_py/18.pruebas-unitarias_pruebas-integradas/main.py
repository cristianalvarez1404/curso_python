import unittest

class BaseDatos:
  def __init__(self):
    self.productos = []

  def guardar(self, producto):
    self.productos.append(producto)

def guardar_pedido(total, base_datos):
  base_datos.guardar({"total":total})

def calcular_total(cantidad, precio):
  return cantidad * precio

def crear_pedido(cantidad, precio, base_datos):
  total = calcular_total(cantidad, precio)
  guardar_pedido(total, base_datos)
  return total

class TestIntegracion(unittest.TestCase):
  def test_integracion(self):
    db = BaseDatos()
    total = crear_pedido(50, 3, db)

    self.assertEqual(total, 150)
    self.assertEqual(db.productos, [{"total":150}])


# class TestTotal(unittest.TestCase):
#   def test_total(self):
#     resultado = calcular_total(50, 3)
#     self.assertEqual(resultado, 150)

if __name__ == "__main__":
  unittest.main()