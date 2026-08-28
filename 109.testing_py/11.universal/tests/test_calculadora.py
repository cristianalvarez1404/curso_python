import unittest
from calculadora import sumar

class TestCalculadora(unittest.TestCase):
  def test_suma(self):
    self.assertEqual(sumar(3,2),5)
