import os

print(os.getcwd())
os.makedirs("examples")
os.path.join("cursos","texto.txt")
print(os.path.getsize("operaciones.py"))
os.rename("operaciones.py","operaciones2.py")
os.remove("texto.txt")
print(os.path.exists("operaciones2.py"))