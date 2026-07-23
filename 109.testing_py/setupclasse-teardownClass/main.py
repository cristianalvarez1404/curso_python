import unittest
from conexion import Conexion

class TestSQL(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    cls.db = Conexion().conectar()
    cls.numero = 5
    
  # def setUp(self):
  #   self.db = Conexion().conectar()

  @classmethod
  def tearDownClass(cls):
    cls.db = Conexion().desconectar()
    cls.numero = 5

  # def tearDown(self):
  #   self.db = Conexion().desconectar()

  def test_query1(self):
    print("Test Query1...")
    print(self.numero)

  def test_query2(self):
    print("Test Query2...")
    print(self.numero)

  def test_query3(self):
    print("Test Query3...")
    print(self.numero)

if __name__ == "__main__":
  unittest.main()