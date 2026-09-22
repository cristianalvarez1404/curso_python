import unittest
import os

class TestArchivo(unittest.TestCase):

  def setUp(self):
    self.nombre_archivo = "temporal.txt"
    self.archivo = open(self.nombre_archivo, "w")

    self.addCleanup(os.remove, self.nombre_archivo)
    self.addCleanup(self.archivo.close)

  # def tearDown(self):
  #   self.archivo.close()
  #   os.remove(self.nombre_archivo)

  def test_archivo(self):
    self.archivo.write("Hola mundo")

    self.assertTrue(os.path.exists(self.nombre_archivo))

if __name__ == "__main__":
  unittest.main()