from infrastructure.repositories.sql_user import SQLRespository
from application.use_case.create_user import CreateUser
from principal.controllers.user_controller import UserController

repository = SQLRespository()
create_user = CreateUser(repository)
controller = UserController(create_user)

controller.create("Jhon")