from domain.entities.user import User
from domain.repositories.user_repository import UserRespository

class CreateUser:
  def __init__(self, repository:UserRespository):
    self.repository = repository

  def execute(self, name):
    user = User(name)
    self.repository.save(user)
    return user