from services.product_service import ProductService

class ProductController:
  def __init__(self):
    self.service = ProductService()

  def create(self, nombre, precio):
    self.service.create_product(nombre=nombre, precio=precio)
  
  def get_product(self):
    return self.service.get_all_products()

