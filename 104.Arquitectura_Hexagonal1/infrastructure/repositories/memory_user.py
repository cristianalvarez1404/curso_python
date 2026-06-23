from domain.repositories.user_repository import UserRepository

class MemoryRepository:
  def __init__(self):
    self.users = []
  
  def save(self, user:UserRepository):
    self.users.append(user)
    print("Usuario almacenado en memoria")