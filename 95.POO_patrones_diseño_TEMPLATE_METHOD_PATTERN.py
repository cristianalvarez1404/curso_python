
class PaginaWeb:
  def renderizar(self):
    self.navbar()
    self.contenido()
    self.footer()

  def navbar(self):
    print("Navbar principal...")

  def contenido(self):
    pass

  def footer(self):
    print("Footer principal")

class PaginaInicio(PaginaWeb):
  def contenido(self):
    print("Pagina inicio...")

class PaginaContacto(PaginaWeb):
  def contenido(self):
    print("Formulario de contacto....")

pagina = PaginaWeb()
p_inicio = PaginaInicio()
p_contacto = PaginaContacto()

# pagina.renderizar()
# p_inicio.renderizar()
p_contacto.renderizar()