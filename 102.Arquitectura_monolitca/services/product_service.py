from models.product import Product
from repositories.product_repository import ProductRepository

class ProductService:
  def __init__(self):
    self.repository = ProductRepository()

  def create_product(self, nombre, precio):
    product = Product(nombre=nombre, precio=precio)
    self.repository.save(product=product)

  def get_all_products(self):
    return self.repository.get_all()
