
class Carrito:
  def __init__(self,productos):
    self.productos = productos

  def __len__(self):
    return len(self.productos)

  def __setitem__(self,index,valor):
    self.productos[index] = valor

  def __getitem__(self, index):
    return self.productos[index]
  
  def __delitem__(self,index):
    del self.productos[index]

  def __call__(self,index):
    return self.productos[index]

  def __bool__(self):
    return len(self.productos) > 0


c1 = Carrito([])
c1[0] = "Producto100"
del c1[2]
print(c1.productos)
l = [1,2,3,4,5]
print(len(c1))
print(c1[0])
print(c1(0))

if c1:
  print("Tiene productos el carrito")
else:
  print("No tiene productos el carrito")
