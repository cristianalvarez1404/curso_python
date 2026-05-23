
class VideoService:
  def ver_curso(self, curso):
    print(f"Cargando curso de {curso}")

class ProxyVideo:
  def __init__(self):
    self.service = VideoService()

  def ver_curso(self, video, es_premium):
    if not es_premium:
      print("El curso es de pago.")
      return
    
    self.service.ver_curso(video)

# proxy_video = ProxyVideo()
# proxy_video.ver_curso("Python",False)
# proxy_video.ver_curso("Python",True)


# video_service = VideoService()
# video_service.ver_curso("Python")

class WebClima:
  def consultar_clima(self):
    print("Cargando información del clima")
    return "20 grados"
  
class ProxyClima:
  def __init__(self):
    self.cache = None

  def consultar_clima(self):
    if self.cache is not None:
      print("Cargando información desde cache...")
      return self.cache

    print("Consultando web del clima...")
    self.cache = "20 grados"
    return self.cache

proxy_clima = ProxyClima()
print(proxy_clima.consultar_clima()  )
print(proxy_clima.consultar_clima()  )





