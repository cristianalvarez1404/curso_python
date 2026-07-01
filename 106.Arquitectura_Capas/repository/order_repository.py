from database.db_orders import DatabaseOrders

class OrderRepository:
  def __init__(self):
    self.db = DatabaseOrders()

  def create_order(self, order):
    print("Capa repository")
    self.db.save(order)

    


