
class BookController:
  def __init__(self, register):
    self.register = register

  def create(self, title):
    self.register.execute(title = title)

    return {
      "title": title
    }