
texto = "hola MUNDO"

print(type(texto))
texto1 = texto.upper()
texto1 = texto.lower()
texto1 = texto.capitalize()
texto1 = texto.title()
print(texto1)

texto = "Programando en JS"
texto1 = texto.replace("JS","Python")
texto1 = texto.count("a")
print(texto1)

texto = " hola "
texto1 = texto.lstrip()
texto1 = texto.rstrip()
texto1 = texto.strip()
print(texto1)

texto = "Manzana,Uvas,Peras"
texto1 = texto.split(",")
texto1 = "-".join(texto1)
print(texto1)

texto = "a"

print(texto.isdigit())
print(texto.isalnum())
print(texto.isalpha())
print(texto.isspace())