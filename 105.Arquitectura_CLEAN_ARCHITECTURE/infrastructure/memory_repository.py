
class MemoryRepository:
  def __init__(self):
    self.books = []

  def save(self, book):
    self.books.append(book)
    print("Libro almacenado en memoria!")