from application.use_case.create_user import CreateUser

class UserController:
  def __init__(self, create_user:CreateUser):
    self.create_user = create_user
  
  def create(self, name):
    self.create_user.execute(name)