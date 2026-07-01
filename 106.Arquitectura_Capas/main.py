from controllers.order_controller import OrderController

controller = OrderController()

request = {
  "cliente":"Jhon",
  "cantidad":5,
}

controller.create_new_order(request)