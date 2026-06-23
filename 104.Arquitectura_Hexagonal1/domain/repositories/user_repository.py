from typing import Protocol
from domain.entities.user import User

class UserRepository(Protocol):
  def save(self, user:User):
    ...
