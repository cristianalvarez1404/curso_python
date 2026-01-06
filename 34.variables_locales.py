x = 10

def padre():
  # global x
  x = 15

  def hijo():
    nonlocal x
    x = 20
    print(x)

  hijo()
  print(x)

padre()
