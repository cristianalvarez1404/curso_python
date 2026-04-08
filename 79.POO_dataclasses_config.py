from dataclasses import dataclass,field

@dataclass(order=True,frozen=True)
class Usuario:
  nombre:str = field(compare=False)
  edad:int
  password:str = field(repr=False,compare=False)

u1 = Usuario("usuario1",35,"123")
u2 = Usuario("usuario2",35,"456")

# u1.password = "12345"

print(u1 >= u2)

