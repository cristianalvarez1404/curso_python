from entities.book import Book

class RegisterBook:
  def __init__(self, repository):
    self.repository = repository

  def execute(self, title):
    book = Book(title=title)

    if not book.is_valid():
      raise Exception("Titulo invalido")
    
    self.repository.save(book)
  
    return book