class UserRepository:
  def obtener_usuario(self, id):
    print("Conectando a MYSQL...")
    print(f"SELECT * FROM users WHERE id = {id}")

    usuario = {
      "id":1,
      "nombre":"Jhon"
    }

    return usuario
  
class MySQLRepository:
  def obtener_usuario(self, id):
    print("Conectando a MYSQL...")
    print(f"SELECT * FROM users WHERE id = {id}")

    usuario = {
      "id":1,
      "nombre":"Jhon"
    }

    return usuario
  
class MongoRepository:
  def obtener_usuario(self, id):
    print("Conectando a MongoDB...")
    print(f"SELECT * FROM users WHERE id = {id}")

    usuario = {
      "id":1,
      "nombre":"Jhon"
    }

    return usuario
  

class UserService:
  def __init__(self, repo):
    self.repo = repo

  def obtener_usuario(self, id):
    return self.repo.obtener_usuario(id)
  
# u_service = UserService(UserRepository())
u_service = UserService(MongoRepository())

print(u_service.obtener_usuario(1))