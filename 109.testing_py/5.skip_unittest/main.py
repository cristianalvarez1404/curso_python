import unittest

num = 20

class Test(unittest.TestCase):

  @unittest.skip("Test en mantenimiento...")
  def test_suma(self):
    self.assertEqual(4+2, 6)

  def test_restar(self):
    self.assertEqual(4-2, 2)

  @unittest.skipIf(num > 10, "Test no se ejecuta..." )
  def test_multiplicar(self):
    self.assertEqual(5*2, 10)

  @unittest.skipUnless(num > 10, "Test no se ejecuta..." )
  def test_multiplicar2(self):
    self.assertEqual(5*2, 10)

if __name__ == "__main__":
  unittest.main(verbosity=2)
