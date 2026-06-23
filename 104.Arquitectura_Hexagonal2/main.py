from infrastructure.respositories.memory_user import MemoryRepository
from infrastructure.respositories.sql_user import SQLRepository
from application.use_case.create_user import CreateUser
from principal.controllers.user_controller import UserController

# repository = SQLRepository()
repository = MemoryRepository()
create_user = CreateUser(repository=repository)
controller = UserController(create_user=create_user)

controller.create("Jhon")
