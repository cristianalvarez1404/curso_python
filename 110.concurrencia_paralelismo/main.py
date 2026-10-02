import asyncio

# def tareas(tarea):
#   print(f"Iniciando tarea: {tarea}")
#   print(f"Finalizando tarea: {tarea}")

# tareas("A")
# tareas("B")
# tareas("C")


lista = ["A","B","C"]

for i in range(3):
  for tarea in lista:
    print(f"Tarea: {tarea} - {i + 1}")
