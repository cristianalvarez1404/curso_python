
class MemoryRepository:
  def __init__(self):
    self.users = []

  def save(self, user):
    self.users.append(user)
    print("Usuario almacenado en memoria")