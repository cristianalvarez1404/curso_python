import unittest

numeros = [2,4,8,7,9,10,13]

class TestOperacion(unittest.TestCase):

  def test_es_par(self):
    for n in numeros:
      with self.subTest(numeros = n):
        self.assertEqual(n % 2, 0)

if __name__ == "__main__":
  unittest.main()