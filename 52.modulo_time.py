import time
import datetime

print("Inicio")
time.sleep(2)
print("Final")

inicio = time.time()

for _ in range(10000000):
  pass

final = time.time()
print(f"Tiempo => {final - inicio}")

fecha = time.time()
print(time.ctime(fecha))



