
class ConexionDB:
  _instancia = None

  def __new__(cls):
    if cls._instancia is None:
      cls._instancia = super().__new__(cls)
    else:
      print("Reutilizando conexión DB...")
    return cls._instancia

  def conectar(self):
    print("Conectando a la base de datos...")


conexion1 = ConexionDB()
conexion1.conectar()

conexion2 = ConexionDB()
conexion2.conectar()

print(conexion1 == conexion2)