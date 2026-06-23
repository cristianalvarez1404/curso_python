from domain.entities.user import User
from domain.repositories.user_repository import UserRepository

class CreateUser:
  def __init__(self, repository:UserRepository):
    self.repository = repository

  def execute(self, name):
    user = User(name)
    self.repository.save(user)
    return user