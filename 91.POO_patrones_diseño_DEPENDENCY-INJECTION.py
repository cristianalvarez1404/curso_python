from abc import ABC, abstractmethod

class Database(ABC):
  @abstractmethod
  def save(self):
    pass

class MySQLDatabase(Database):
  def save():
    print("Guardando con MySQL...")

class PostregreSQLDatabase(Database):
  def save():
    print("Guardando con PostgreSQL...")

class UserService:
  def __init__(self, db:Database):
    self.db = db

  def save_user(self):
    self.db.save()

db1 = MySQLDatabase()
db2 = PostregreSQLDatabase()

user_service = UserService(PostregreSQLDatabase)
user_service.save_user()