import warnings
import unittest

def analizar_datos(elementos):
    if len(elementos) < 10:
        warnings.warn("Se recomienda un longitud >= 10 elementos para mayor precision", UserWarning)

    return sum(elementos)


class TestDatos(unittest.TestCase):

  def test_elementos(self):
    with self.assertWarns(UserWarning):
      resultado = analizar_datos([1,2,3])

    self.assertEqual(resultado, 6)

if __name__ == "__main__":
   unittest.main()
      