from typing import Protocol

class Reader(Protocol):
  def read(self):
    ...

class TXTReader:
  def read_txt(self):
    print("Leyendo TXT")

class JSONReader:
  def to_Json(self):
    print("Leyendo JSON")

class XMLReader:
  def to_xlm(self):
    print("Leyendo XML")

class TXTAdapter:
  def __init__(self, txtReader):
    self.reader = txtReader

  def read(self):
    self.reader.read_txt()

class JSONAdapter:
  def __init__(self, jsonReader):
    self.reader = jsonReader

  def read(self):
    self.reader.to_Json()

class XMLAdapter:
  def __init__(self, xmlReader):
    self.reader = xmlReader

  def read(self):
    self.reader.to_xlm()


def leer_archivo(reader:Reader):
  reader.read()


txt = TXTAdapter(TXTReader())
json = JSONAdapter(JSONReader())
xml = XMLAdapter(XMLReader())

leer_archivo(txt)
leer_archivo(json)
leer_archivo(xml)



# def leer_archivo(reader, tipo):
#   if tipo == "txt":
#     reader.read_txt()
#   elif tipo == "json":
#     reader.to_Json()
#   else:
#     print("Archivo no valido")

# # leer_archivo(TXTReader(),"txt")
# leer_archivo(JSONReader(),"json")