from infrastructure.memory_repository import MemoryRepository
from infrastructure.sql_repository import SQLRepository
from controllers.book_controller import BookController
from use_cases.register_book import RegisterBook

# repository = MemoryRepository()
repository = SQLRepository()
register = RegisterBook(repository=repository)
controller = BookController(register=register)

response = controller.create("Titulo 1")

print(response)
