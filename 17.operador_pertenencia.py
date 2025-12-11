#membership operators

num1 = [5,10,15,20]
var = 50

print(15 in num1 )
print(17 in num1 )
print(25 not in num1 )

if var not in num1:
  num1.append(var)
  print("Se ha agregado el elemento")
else:
  print("Elemento ya se encuentra en la lista")

print(num1)