from typing import Protocol
from domain.entities.user import User

class UserRespository(Protocol):
  def save(self, user:User):
    ...