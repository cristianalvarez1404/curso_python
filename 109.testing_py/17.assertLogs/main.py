import logging
import unittest

#DEBUG
#INFO
#WARNING
#ERROR
#CRITICAL

logging.basicConfig(filename="app.log",level=logging.INFO)

def procesar_pago():
  #logging.info("Procesando pago...")
  #codigo
  logging.warning("Pago rechazado")
  #logging.info("Pago finalizado!")

class TestPago(unittest.TestCase):
  def test_pago(self):
    with self.assertLogs(level="WARNING") as log:
      procesar_pago()

    self.assertIn("Pago rechazado", log.output[0])

if __name__ == "__main__":
  unittest.main()