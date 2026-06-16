from controllers.product_controller import ProductController


controller = ProductController()

controller.create("product1",100)
controller.create("product2",200)
controller.create("product3",300)

products = controller.get_product()

for product in products:
  print(f"Product: {product.nombre} - precio: {product.precio}")
