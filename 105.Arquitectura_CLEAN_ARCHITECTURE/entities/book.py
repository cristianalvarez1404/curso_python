class Book:
  def __init__(self, title):
    self.title = title

  def is_valid(self):
    return self.title != ""
  