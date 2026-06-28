from abc import ABC, abstractmethod

class BookRepository(ABC):
  @abstractmethod
  def save(self, book):
    pass