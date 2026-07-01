from repository.order_repository import OrderRepository

class OrderService:
  def __init__(self):
    self.repository = OrderRepository()

  def create(self, order):
    
    if order["cantidad"] < 0:
      print("Cantidad no permitida")
      return
    
    print("Orden validada!")

    self.repository.create_order(order)
    
    