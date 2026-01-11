
def suma(*args):
  sum = 0
  for i in args:
    sum += i

  return sum

print(suma(1,2,3,2))