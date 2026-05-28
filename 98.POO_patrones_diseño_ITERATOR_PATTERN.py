import random

class Playlist:
  def __init__(self):
    self.lista = []

  def add(self, cancion):
    self.lista.append(cancion)

  def __iter__(self):
    lista_aleatoria = self.lista.copy()
    random.shuffle(lista_aleatoria)

    return iter(lista_aleatoria)

playlist = Playlist()
playlist.add("cancion1")
playlist.add("cancion2")
playlist.add("cancion3")

for cancion in playlist:
  print(cancion)


# lista_canciones = ["cancion1","cancion2","cancion3"]

# for cancion in lista_canciones:
#   print(cancion)