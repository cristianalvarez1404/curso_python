from services.order_service import OrderService

class OrderController:

  def __init__(self):
    self.service = OrderService()

  def create_new_order(self, order):
    print("Enviando información al service...")
    self.service.create(order)