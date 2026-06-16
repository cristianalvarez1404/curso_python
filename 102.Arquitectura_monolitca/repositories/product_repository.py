from database.db import products

class ProductRepository:
  def save(self, product):
    products.append(product)

  def get_all(self):
    return products